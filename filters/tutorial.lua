-- One manuscript: questions/reveals in Beamer, full explanations elsewhere.
-- .detail is supplementary prose for the article and website.
-- .question/.answer occupy successive overlays of the same frame.
local function has_class(element, name)
  return element.classes:includes(name)
end

-- Keep descriptive captions in the manuscript and HTML. On slides, the
-- heading and adjacent teaching text already explain each diagram.
function Figure(element)
  if FORMAT == 'beamer' then
    return element.content
  end
end

function CodeBlock(element)
  if FORMAT == 'latex' and has_class(element, 'powershell') then
    return pandoc.RawBlock('latex', '\\begin{Verbatim}[breaklines=true,breakanywhere=true]\n'
      .. element.text .. '\n\\end{Verbatim}')
  end
end

function Div(element)
  if FORMAT ~= 'beamer' then
    return nil
  end
  if has_class(element, 'detail') then
    return {}
  end
  local overlay
  if has_class(element, 'question') then overlay = '1' end
  if has_class(element, 'answer') then overlay = '2' end
  if overlay then
    local blocks = pandoc.List({pandoc.RawBlock('latex', '\\begin{onlyenv}<' .. overlay .. '>')})
    blocks:extend(element.content)
    blocks:insert(pandoc.RawBlock('latex', '\\end{onlyenv}'))
    return blocks
  end
  if has_class(element, 'prompt') then
    local blocks = pandoc.List({pandoc.RawBlock('latex', '\\begingroup\\large\\bfseries')})
    blocks:extend(element.content)
    blocks:insert(pandoc.RawBlock('latex', '\\endgroup'))
    return blocks
  end
end
