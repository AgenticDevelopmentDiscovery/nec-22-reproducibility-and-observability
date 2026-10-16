"""Offline symbolic-regression agent with manifests, replay, and divergence reports."""

import argparse
import ast
import hashlib
import json
import operator
from pathlib import Path
import platform
import random
import subprocess
import sys
import time
from datetime import datetime, timezone
from uuid import uuid4


MODEL_ID = "offline-rule-agent-v1"
PROMPT = "Find an equation with minimum mean squared error; retain the best candidate."
DATA = [{"x": x, "y": x * x + 1} for x in [-2, -1, 0, 1, 2]]
CONFIG = {"model_id": MODEL_ID, "seed": 7, "temperature": None, "top_p": None,
          "prompt": PROMPT, "metric": "mean_squared_error", "retry_limit": 0,
          "candidate_budget": 5, "execution": "serial", "corpus_snapshot": None}


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def digest(value):
    return hashlib.sha256(encoded(value)).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def now():
    return datetime.now(timezone.utc).isoformat()


def code_hash():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def git_state():
    try:
        root = Path(__file__).resolve().parent
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root,
                                         stderr=subprocess.DEVNULL, text=True).strip()
        dirty = bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=root,
                                             stderr=subprocess.DEVNULL, text=True).strip())
        return {"commit": commit, "dirty": dirty}
    except (OSError, subprocess.CalledProcessError):
        return {"commit": None, "dirty": None}


def evaluate(expression, x):
    """Interpret a tiny arithmetic grammar; never execute candidate source code."""
    operations = {ast.Add: operator.add, ast.Sub: operator.sub,
                  ast.Mult: operator.mul, ast.Div: operator.truediv}

    def visit(node):
        if isinstance(node, ast.Name) and node.id == "x":
            return x
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -visit(node.operand)
        if isinstance(node, ast.BinOp) and type(node.op) in operations:
            return operations[type(node.op)](visit(node.left), visit(node.right))
        raise ValueError("Unsupported equation syntax")

    return visit(ast.parse(expression, mode="eval").body)


def proposal(step, best, rng):
    if step == 1:
        return "x", None
    if step == 2:
        return f"({best['equation']}) * ({best['equation']})", best["candidate_id"]
    if step == 3:
        return f"({best['equation']}) + 1", best["candidate_id"]
    if step == 4:
        return "1 / x", None
    return f"({best['equation']}) + ({rng.choice([-2, -1, 1, 2])})", best["candidate_id"]


def run(out, dataset=None, config=None, parent=None, change=None):
    dataset = DATA if dataset is None else dataset
    config = dict(CONFIG if config is None else config)
    if set(config) != set(CONFIG) or any(config[k] != CONFIG[k] for k in CONFIG if k != "seed"):
        raise ValueError("Unsupported agent configuration")
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)  # Never overwrite run evidence.
    run_id = uuid4().hex
    manifest = {"schema_version": 1, "run_id": run_id, "parent_run_id": parent,
                "created_at": now(), "status": "running", "config": config,
                "config_hash": digest(config), "dataset": dataset,
                "dataset_hash": digest(dataset), "code_sha256": code_hash(),
                "code_snapshot": "agent.py", "git": git_state(),
                "runtime": {"python": platform.python_version(), "platform": platform.platform()},
                "change": change, "steps": "steps.jsonl", "result": "result.json"}
    (out / "agent.py").write_bytes(Path(__file__).read_bytes())
    write_json(out / "manifest.json", manifest)
    rng = random.Random(config["seed"])
    best = None
    failures = 0
    try:
        with (out / "steps.jsonl").open("w", encoding="utf-8") as log:
            for step in range(1, config["candidate_budget"] + 1):
                started = time.perf_counter()
                equation, parent_candidate = proposal(step, best, rng)
                event = {"run_id": run_id, "trace_id": run_id, "span_id": f"c{step:03}",
                         "parent_span_id": "run", "step": step, "attempt": 1,
                         "candidate_id": f"c{step:03}", "parent_candidate_id": parent_candidate,
                         "started_at": now(), "equation": equation,
                         "inputs": {"dataset_hash": manifest["dataset_hash"],
                                    "config_hash": manifest["config_hash"], "incumbent": best},
                         "predictions": [], "score": None, "status": "ok", "error": None}
                try:
                    for row in dataset:
                        event["predictions"].append(evaluate(equation, row["x"]))
                    event["score"] = sum((p - row["y"]) ** 2 for p, row in
                                         zip(event["predictions"], dataset)) / len(dataset)
                except (ArithmeticError, ValueError) as error:
                    failures += 1
                    event["status"] = "error"
                    event["error"] = {"type": type(error).__name__, "message": str(error),
                                      "row_index": len(event["predictions"])}
                if event["status"] == "ok" and (best is None or event["score"] < best["score"]):
                    best = {"candidate_id": event["candidate_id"], "equation": equation,
                            "score": event["score"]}
                event["duration_ms"] = round((time.perf_counter() - started) * 1000, 3)
                log.write(json.dumps(event, allow_nan=False) + "\n")
                log.flush()
        result = {"run_id": run_id, "parent_run_id": parent,
                  "dataset_hash": manifest["dataset_hash"], "config_hash": manifest["config_hash"],
                  "best": best, "attempted": config["candidate_budget"], "failed": failures}
        write_json(out / "result.json", result)
        manifest["status"] = "completed_with_errors" if failures else "completed"
    except Exception as error:
        manifest["status"] = "failed"
        manifest["error"] = {"type": type(error).__name__, "message": str(error)}
        raise
    finally:
        manifest["finished_at"] = now()
        write_json(out / "manifest.json", manifest)
    return manifest


def validate(manifest_path):
    manifest_path = Path(manifest_path)
    manifest = read_json(manifest_path)
    if manifest["schema_version"] != 1:
        raise ValueError("Unsupported manifest schema")
    for name in ("dataset", "config"):
        if digest(manifest[name]) != manifest[name + "_hash"]:
            raise ValueError(f"{name} hash mismatch: manifest was changed")
    snapshot_hash = hashlib.sha256((manifest_path.parent / "agent.py").read_bytes()).hexdigest()
    if snapshot_hash != manifest["code_sha256"] or code_hash() != manifest["code_sha256"]:
        raise ValueError("Code hash mismatch: replay with the unchanged saved agent.py")
    if manifest["runtime"]["python"] != platform.python_version():
        raise ValueError("Python version mismatch: use the recorded runtime")
    if manifest["status"] not in ("completed", "completed_with_errors"):
        raise ValueError("Source run did not complete")
    return manifest


def replay(manifest_path, out, corrupt=False):
    source = validate(manifest_path)
    dataset = source["dataset"]
    change = None
    if corrupt:
        before = dataset[0]["y"]
        dataset[0]["y"] = before + 1
        change = {"purpose": "deliberate divergence experiment", "field": "dataset[0].y",
                  "before": before, "after": before + 1}
    return run(out, dataset, source["config"], source["run_id"], change)


def differences(left, right, prefix=""):
    if isinstance(left, dict) and isinstance(right, dict):
        found = []
        for key in sorted(left.keys() | right.keys()):
            path = f"{prefix}.{key}" if prefix else key
            if key not in left or key not in right:
                found.append({"field": path, "before": left.get(key), "after": right.get(key)})
            else:
                found.extend(differences(left[key], right[key], path))
        return found
    return [] if left == right else [{"field": prefix, "before": left, "after": right}]


def compare(left_dir, right_dir):
    left_dir, right_dir = Path(left_dir), Path(right_dir)
    manifests = [read_json(d / "manifest.json") for d in (left_dir, right_dir)]
    for directory in (left_dir, right_dir):
        validate(directory / "manifest.json")
    # These identify this execution, rather than the experiment's behavior.
    volatile = {"run_id", "trace_id", "started_at", "duration_ms"}
    logs = [[{k: v for k, v in json.loads(line).items() if k not in volatile}
             for line in (d / "steps.jsonl").read_text(encoding="utf-8").splitlines()]
            for d in (left_dir, right_dir)]
    first = None
    for index in range(max(map(len, logs))):
        a = logs[0][index] if index < len(logs[0]) else None
        b = logs[1][index] if index < len(logs[1]) else None
        changed = differences(a, b)
        if changed:
            first = {"step": index + 1, "changes": changed}
            break
    experiment_fields = ("dataset_hash", "config_hash", "code_sha256", "runtime")
    manifest_changes = differences(*[{k: m[k] for k in experiment_fields} for m in manifests])
    results = [read_json(d / "result.json") for d in (left_dir, right_dir)]
    result_changes = differences(*[{k: v for k, v in r.items() if k not in
                                   ("run_id", "parent_run_id")} for r in results])
    return {"match": not (manifest_changes or first or result_changes),
            "manifest_changes": manifest_changes, "first_step_difference": first,
            "result_changes": result_changes,
            "compared_steps": min(map(len, logs)) if first is None else first["step"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("run")
    create.add_argument("--out", required=True)
    create.add_argument("--seed", type=int, default=7)
    for name in ("replay", "corrupt"):
        command = commands.add_parser(name)
        command.add_argument("manifest")
        command.add_argument("--out", required=True)
    diff = commands.add_parser("compare")
    diff.add_argument("left")
    diff.add_argument("right")
    args = parser.parse_args()
    try:
        if args.command == "compare":
            report = compare(args.left, args.right)
            print(json.dumps(report, indent=2))
            return 0 if report["match"] else 1
        if args.command == "run":
            manifest = run(args.out, config={**CONFIG, "seed": args.seed})
        else:
            manifest = replay(args.manifest, args.out, args.command == "corrupt")
        print(f"{manifest['status']}: {args.out}/manifest.json")
        return 0
    except (ValueError, OSError, KeyError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
