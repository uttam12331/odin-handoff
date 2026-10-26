# Odin handoff

Everything needed to continue work on **Mercor Project Odin**: the rules, our
recording scripts, the task files and the exact point where we stopped.

> **Use your own accounts.** Every writer needs their own Mercor/Okta login, OTA
> account, Insightful timer and Studio tasks. Don't record or submit on another
> person's account. The tasks below are listed so you can learn from them and
> reuse the method, not so you can submit them as someone else.

## Start here

1. Read **[HANDOFF.md](HANDOFF.md)**. It covers where we are, what failed and what to do next.
2. Read **[skills/odin/SKILL.md](skills/odin/SKILL.md)**. It has every Odin rule we've
   collected, plus lessons from reviewer feedback.
3. For your own first task, follow **[guides/Odin_Starter_Guide.html](guides/Odin_Starter_Guide.html)**
   (open it in a browser). It covers accounts, the timer, Mac setup, recording and submitting.

## Use it with Claude Code (to continue "this chat")

Claude remembers the rules through a **skill** and a few **memory notes**. Install them once:

```bash
# from inside this repo
mkdir -p ~/.claude/skills/odin
cp skills/odin/SKILL.md ~/.claude/skills/odin/SKILL.md
```

Then open Claude Code in a working folder and say, for example:

> Load the odin skill and read HANDOFF.md in this repo, then continue from "Next step".

The skill tells Claude how to help:
- label every step **[MAIN]** or **[REC.MAC]**
- give one small step at a time
- give paste-ready text
- write only honest disputes
- accept AI-made inputs from Gemini only

When you tell Claude a **new Odin rule**, it updates `SKILL.md` and adds a dated line to
its **Rules log**. Commit that file back to this repo so everyone gets the update.

`claude-memory/` has the two memory notes from the original chat. They're optional;
the skill already contains everything in them.

## What's in this repo

| Path | What it is |
|---|---|
| `HANDOFF.md` | Current status, history and the next step |
| `skills/odin/SKILL.md` | All Odin rules, workflow, lessons, task history, rules log |
| `guides/Odin_Starter_Guide.html` | Beginner guide: accounts, Insightful, Mac setup, screen rules, recording, submitting |
| `tasks/3kuwe593-library-api/` | Library API task: recording script (`.txt` + colour `.html` for a phone), `Metadata.rtf`, starting code and finished code |
| `tasks/veiw1b03-returns-analysis/` | Data-analysis task (on hold): scripts, SQL, notebook code |
| `scripts/txt_to_colour_html.py` | Turns a `.txt` script into the phone-friendly colour HTML (`python txt_to_colour_html.py in.txt out.html`) |
| `claude-memory/` | Memory notes from the original Claude session |

## Not included (on purpose)

- **The Writer Guidelines PDF.** It's a project document. Get the current version through
  Okta → Google Drive. `SKILL.md` summarises what matters.
- **Recordings, passwords and personal files.** Never commit OTA passwords, recordings or
  anything with personal information to this repo.
