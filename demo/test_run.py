"""Behavior checks for the tutorial's replay and failure claims."""

import json
from pathlib import Path
import tempfile
import unittest

from run import compare, read_json, replay, run, write_json


class DemoTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.original = self.root / "original"
        run(self.original)

    def test_replay_matches_and_retains_failed_candidate(self):
        repeat = self.root / "repeat"
        replay(self.original / "manifest.json", repeat)
        self.assertTrue(compare(self.original, repeat)["match"])
        result = read_json(repeat / "result.json")
        self.assertEqual(result["best"]["score"], 0)
        self.assertEqual((result["attempted"], result["failed"]), (5, 1))
        events = [json.loads(line) for line in (repeat / "steps.jsonl").read_text().splitlines()]
        failed = events[3]
        self.assertEqual(failed["error"]["type"], "ZeroDivisionError")
        self.assertEqual(failed["error"]["row_index"], 2)
        self.assertEqual(failed["predictions"], [-0.5, -1.0])
        self.assertIsNone(failed["score"])
        self.assertEqual(events[2]["parent_candidate_id"], "c002")
        self.assertEqual(read_json(repeat / "manifest.json")["parent_run_id"],
                         read_json(self.original / "manifest.json")["run_id"])

    def test_changed_input_pinpoints_first_changed_score(self):
        changed = self.root / "changed"
        replay(self.original / "manifest.json", changed, corrupt=True)
        report = compare(self.original, changed)
        self.assertFalse(report["match"])
        self.assertEqual(report["first_step_difference"]["step"], 1)
        score_change = next(c for c in report["first_step_difference"]["changes"]
                            if c["field"] == "score")
        self.assertEqual((score_change["before"], score_change["after"]), (13.8, 16.8))
        self.assertEqual(read_json(self.original / "manifest.json")["dataset"][0]["y"], 5)

    def test_rejects_tampering_and_overwrite(self):
        manifest_path = self.original / "manifest.json"
        manifest = read_json(manifest_path)
        manifest["dataset"][0]["y"] = 100
        write_json(manifest_path, manifest)
        with self.assertRaisesRegex(ValueError, "dataset hash mismatch"):
            replay(manifest_path, self.root / "invalid")
        self.assertFalse((self.root / "invalid").exists())
        with self.assertRaises(FileExistsError):
            run(self.original)

    def test_compare_catches_missing_step_and_changed_winner(self):
        repeat = self.root / "repeat"
        replay(self.original / "manifest.json", repeat)
        result = read_json(repeat / "result.json")
        result["best"]["score"] = 99
        write_json(repeat / "result.json", result)
        self.assertFalse(compare(self.original, repeat)["match"])
        steps = repeat / "steps.jsonl"
        steps.write_text("\n".join(steps.read_text().splitlines()[:-1]) + "\n")
        self.assertEqual(compare(self.original, repeat)["first_step_difference"]["step"], 5)


if __name__ == "__main__":
    unittest.main()
