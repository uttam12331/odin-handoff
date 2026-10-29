import html, re, sys

src, dst = sys.argv[1], sys.argv[2]
lines = open(src, encoding="utf-8").read().splitlines()

out = []
kind = None  # current block kind for continuation lines
i = 0
while i < len(lines):
    line = lines[i]
    s = line.strip()
    if s.startswith("====="):
        # heading block: ===== / title / =====
        if i + 2 < len(lines) and lines[i + 2].strip().startswith("====="):
            out.append(f'<h2>{html.escape(lines[i + 1].strip())}</h2>')
            i += 3
            kind = None
            continue
        i += 1
        continue
    if s.startswith("----") and s.endswith("----"):
        out.append(f'<h3>{html.escape(s.strip("- ").strip())}</h3>')
        kind = None
        i += 1
        continue
    if not s:
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        if kind == "type" and nxt.startswith("      ") and nxt.strip():
            out.append('<div class="type cont"><span class="lbl"></span><span class="txt"> </span></div>')
            i += 1
            continue
        kind = None
        out.append('<div class="gap"></div>')
        i += 1
        continue
    m = re.match(r"^(SAY AFTER|SAY|TYPE|DO|BEFORE|WHILE TYPING)(\s*\([^)]*\))?\s*:\s?(.*)$", s)
    if m:
        kind = {"before": "say", "while typing": "say", "say after": "say"}.get(m.group(1).lower(), m.group(1).lower())
        label = m.group(1) + (m.group(2) or "")
        body = html.escape(m.group(3))
        out.append(f'<div class="{kind}"><span class="lbl">{html.escape(label)}</span>'
                   f'<span class="txt">{body}</span></div>')
    elif kind and line.startswith(" "):
        text = line[6:] if (kind == "type" and line.startswith("      ")) else s
        out.append(f'<div class="{kind} cont"><span class="lbl"></span>'
                   f'<span class="txt">{html.escape(text)}</span></div>')
    else:
        kind = None
        out.append(f'<div class="plain">{html.escape(line)}</div>')
    i += 1

page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Library API Script</title>
<style>
:root {{ --bg:#ffffff; --fg:#1d1d1f; --muted:#6e6e73; --say:#0a7d32; --saybg:#e8f7ed;
        --type:#1d4ed8; --typebg:#eef3ff; --do:#1d1d1f; --h:#7c2d12; --line:#e5e5ea; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#111214; --fg:#ececec; --muted:#9a9aa0; --say:#5fe08a; --saybg:#12301d;
  --type:#8fb2ff; --typebg:#16203a; --do:#ececec; --h:#ffb58a; --line:#2a2b2f; }} }}
:root[data-theme="dark"] {{ --bg:#111214; --fg:#ececec; --muted:#9a9aa0; --say:#5fe08a; --saybg:#12301d;
  --type:#8fb2ff; --typebg:#16203a; --do:#ececec; --h:#ffb58a; --line:#2a2b2f; }}
body {{ background:var(--bg); color:var(--fg); font:16px/1.5 -apple-system, system-ui, sans-serif;
       margin:0 auto; max-width:820px; padding:12px 16px 60px; }}
h2 {{ color:var(--h); font-size:18px; border-bottom:2px solid var(--line); padding-bottom:4px; margin:28px 0 8px; }}
h3 {{ font-size:15px; color:var(--muted); margin:16px 0 4px; }}
.legend {{ position:sticky; top:0; background:var(--bg); padding:8px 0; border-bottom:1px solid var(--line);
          font-size:14px; z-index:2; }}
.legend span {{ margin-right:12px; }}
.gap {{ height:6px; }}
.say, .type, .do {{ display:flex; gap:8px; }}
.lbl {{ flex:0 0 48px; font-weight:700; font-size:12px; padding-top:3px; }}
.txt {{ flex:1; white-space:pre-wrap; overflow-wrap:anywhere; }}
.say {{ background:var(--saybg); border-left:4px solid var(--say); padding:2px 8px; }}
.say .txt {{ color:var(--say); font-weight:600; font-size:17px; }}
.say .lbl {{ color:var(--say); }}
.say.cont {{ margin-top:-1px; }}
.type {{ background:var(--typebg); padding:1px 8px; }}
.type .txt {{ font-family:ui-monospace, Menlo, monospace; font-size:13px; color:var(--type); }}
.type .lbl {{ color:var(--type); }}
.do {{ padding:1px 8px; }}
.do .lbl {{ color:var(--muted); }}
.plain {{ white-space:pre-wrap; font-family:ui-monospace, Menlo, monospace; font-size:13px; color:var(--muted);
          overflow-wrap:anywhere; }}
</style></head><body>
<div class="legend"><span style="color:var(--say);font-weight:700">■ SAY = speak</span>
<span style="color:var(--type);font-weight:700">■ TYPE = type code</span>
<span style="color:var(--muted);font-weight:700">■ DO = click</span></div>
{''.join(out)}
</body></html>"""
open(dst, "w", encoding="utf-8").write(page)
print("written", dst)
