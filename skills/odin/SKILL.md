---
name: odin
description: Rules, workflow and lessons for Mercor Project Odin (macOS TaskRecorder screen-recording tasks in Studio). Use for ANY Odin question - task ideas, Studio forms, Mac/TaskRecorder setup, recording scripts, narration, AutoQC results, disputes, Metadata.rtf, deliverables, Insightful/pay. Also use whenever the user states a NEW Odin rule, so it gets saved into this skill.
---

# Project Odin – rules and workflow

The user (and a colleague) record professional macOS workflows for Mercor Project Odin.
Sources, newest wins: the live **Studio task page** > **#odin--announcements / Maven** >
`Project Odin Writer Guidelines.pdf` (Downloads, Oct 3 2026) > older notes.
When something here conflicts with what the user shows from Studio, trust Studio and
update this file (see "Adding new rules").

## How to answer the user
- Label EVERY step with the Mac user: **[MAIN]** (main account: Studio, Slack, Metadata.rtf,
  Google login) or **[REC.MAC]** (recording user: TaskRecorder, task apps, recording).
- One small step at a time, plain words, exact clicks (they are new to macOS). Wait for "done".
- Always give paste-ready text in code blocks (Studio fields, Metadata, disputes, commands).
- Quote the rule + its source (Studio page / guide page) when asked "where is it written".
- Never write misleading disputes or tick checklist boxes that are not true. Disputes must be
  honest; reviewers check them against the video.
- AI-generated inputs must come from **Gemini only** – do not generate task input files yourself.
- Each person must use their **own** Mercor/Okta, OTA, Insightful and Studio account.

## Accounts and pay
- Personal email → Okta sign-in. **@mercor.expert** → Studio, Writer Guidelines, Insightful.
  **OTA** (task.recording.xxx@gmail.com) → only logins shown inside recordings. Never change OTA
  password/2FA/phone. OTA problems → short message to **@Maven in #odin--helpdesk** (public: no passwords).
- Insightful (Workpuls): Odin → Play, minimize; run for all real Odin work (setup, ideas, practice,
  recording, uploads); pause for breaks; never show its window in a recording.
- Pay from 21 Oct 2026: setup up to 3 h; first task $150 on first submission + $250 at Ready for
  Delivery (RFD); Trial = 12 h + 3 h per RFD task, max 3 open tasks; after 3 RFD → Production tiers
  (1× / 1.375× / 1.875×). Paid Wednesdays.

## Mac setup (recording user)
- Separate Admin user "rec.mac" recommended (Studio says optional). Move files via `/Users/Shared`.
- Clock: Menu Bar → Clock Options → seconds + date. Dock: Left/Right, auto-hide OFF, indicators ON.
- Wallpaper not personal and not macOS default; change ≥1 UI element every recording
  (wallpaper, light/dark, accent colour, Dock size, resolution, in-app theme).
- Do Not Disturb on. Desktop clean. Default cursor.
- Accessibility Inspector: Xcode → right-click Dock icon → Open Developer Tool → Accessibility
  Inspector → close window with RED button → dot must stay under 🔍.
- TaskRecorder **2.4.4** (World files in any Studio task; Intel build exists). No login – if it asks
  for sign-in it's an old version. Permissions Accessibility/Screen Recording/Microphone all green
  (per user). Built-in display, mic Standard.
- VS Code: turn OFF "Screen Reader Optimized" (it disables autocomplete); uninstall Copilot/AI chat.
  Homebrew Python 3.15 blocks pip → use venv `~/venvs/analysis`. In VS Code Enter Interpreter Path use the FULL path `/Users/rec.mac/venvs/analysis/bin/python` (`~` is rejected); bottom bar must show "analysis" or the Run button / Testing panel fail with No module named flask.
- DB Browser: close Edit Database Cell / Plot / Remote panels; turn off auto-updates.
- DBeaver: close AI Chat, never click "AI".

## Idea (Studio)
- Studio → Tasks → **+ Create Task**. "Describe your idea" with 5 headings: **Domain/Role, Goal,
  Starting materials, Steps (app named per step), Deliverable**. Apps box: type each app + Enter.
- Apps named in the text MUST match the Apps list exactly (first idea was returned for this).
- ≥3 apps by default (1–2 only for deeply technical work). "Any app fine unless 🚫 RESTRICTED".
- Same task continues after approval ("Idea Approved: Start Recording"). Never create a duplicate.
  To change idea: **Revise idea**. Status flow: Idea Draft → Checking Idea → Idea Returned / Approved
  → Ready for Review → Needs Edits / Review Approved → Ready for Delivery.
- New task ideas must be meaningfully different (goal, inputs, methods, deliverable), not just topic.

## Apps
- Restricted/banned examples: Excel (use Google Sheets / Excel web), Keynote, Pages, Numbers,
  Preview, Terminal app, iMovie, Final Cut, Logic Pro, Calendar, Reminders, LibreOffice
  Calc/Writer/Impress, Adobe Acrobat, FL Studio. **TextEdit banned except creating Metadata.rtf.**
- Safari and Chrome **allowed since 22 Oct 2026** (other browsers still preferred).
- Finder, the Goal-document app and Insightful never count as task apps.
- No AI tools during recording; normal autocomplete is fine.

## Before recording
- Inputs ready before recording; AI-made only with **Gemini**; fictional data (no real people's
  names); CC0/public domain media with source URL.
- **Goal document**: the **Goal paragraph only** (exactly as approved, typos included) shown at the
  start. If Studio's "Intro doc" is empty, make a PDF (title "Task Goal" 20pt bold, text 16pt Arial,
  black on white, no Mercor/Odin/task ID/personal info) and open it in Brave.
- Same Goal text in 3 places: Goal doc, **TaskRecorder Task Description**, **Metadata.rtf Request**.
- **Metadata.rtf** (main user, TextEdit allowed): `Topology: App (LOOKUP|CREATE|MODIFY) -> ...`
  (each visit, repeat apps when returning), `Request:` Goal, `Task Description:` numbered list.
  Delete the red example section. Never show it in a recording. Upload separately.
- TaskRecorder Used Apps must match Studio names exactly (e.g. "Visual Studio Code", not "VS Code").
- Open + log in + load every task app, set **Fill**, minimize. Quit everything else.
- Practise the whole task at least twice; reset files to the starting state afterwards.

## Recording rules
- Length **15:00–50:59** including intro and epilogue (first task: aim 15–20 min).
- Start Recording → minimize TaskRecorder immediately → Goal doc visible → say only
  "I will be beginning my task soon. Here is the workflow I have in mind." (<20 s) → minimize doc.
- One take, no pause. Small slip: say it, fix it, check it. Big mistake: re-record.
- **Epilogue 3–4 min (max 4:00)** for ideas approved after 19 Oct 6 PM PT: how you checked,
  approach, challenges, quality, what you'd do differently.
- **Narration (AutoQC check 24, blocks submit): ≥70% of actions must state 2 of WHAT / WHERE / WHY.**
  - NEVER read code symbols aloud ("def isbn underscore ok bracket..."). It counts as nothing.
  - Before each typed block: one sentence of what + where (line number / panel) + why.
  - While typing: explain the meaning in plain English. Narrate every edit, even typo fixes.
  - Every click: where it is (corner/side/next to what) + what happens after.
  - Reviewers count manually too; "guidelines have no coding exception" for narration.
- **Typing (AutoQC check 19): ≤35% for coding tasks** (≤20% others; checklist says ~30% coding).
  First recording measured 46% → failed. Keep code short, use autocomplete, copy/paste own lines,
  practise for speed.
- **Window overlap (check 17): no window covered >30 s.** Fill, never Full Screen; one window or two
  side by side (~50/50); **minimize the app you leave before opening the next** (first recording
  failed: DB Browser stayed behind VS Code for 268 s). Same-app pop-ups/dialogs are allowed.
- No silence >45 s; mouse not idle >45 s; ~1 s pause after each click; announce every shortcut.
- Never on screen: TaskRecorder (except start/stop), Insightful, Studio/Slack/Mercor/Odin,
  Metadata.rtf, personal info, AI, profanity. English only.

## After recording and submitting
- Stop → wait Stopping → Archiving → **Idle**. Show Recordings → newest `recording_TIMESTAMP`.
- Check video.mp4 start/middle/end; screenshots > 0.5 × video seconds.
- **Never create or rename recording_….zip** – TaskRecorder makes it. Option-drag copies.
- deliverables.zip: `input 1…`, `artifact 1…`, `final output 1…` (keep extensions; code project =
  folder "final output 1"). Remove __pycache__/.pytest_cache. Metadata.rtf NOT inside.
- Studio → **Upload task files**: 4 separate fields (Metadata.rtf, Screen recording MP4,
  Task Recorder zip, Deliverables.zip). Not the "Media → Upload File" box.
- Also fill: Mac/Insightful questions, 5 one-time setup questions, Resolution, Light/Dark,
  Dock position, UI element changed, 3 Confirm boxes, Input and artifact files
  (e.g. "AI-generated file"), Final note (e.g. "…AI-generated with Gemini before recording.").
- AutoQC: Check 1 (files & recording, ~37 checks) then Check 2 (narration) runs ~10 min later.
  "Waiting on a prerequisite" = wait and reload. After re-uploading, use **Run full AutoQC**
  (not "Rerun failing"). Major/"blocks submit" must pass or be disputed; Minor = advice.
- Manual checks: tick only what is true in the video. Then final confirmation → Submit for Review.
- Needs Edits → read Review Feedback + reviewer notes, re-record in the SAME task, replace files.

## Task history (keep updated)
- veiw1b03 – Q3 returns analysis (DBeaver, VS Code, Google Sheets). Approved; ON HOLD because the OTA
  password stopped working (request sent to Maven). Script: `Odin_Task_veiw1b03_Script.md`,
  `Odin_Recording_Script.txt`.
- nkjsf88f – empty Idea Draft created by mistake; never submit it.
- 3kuwe593 – Library API validation (VS Code, Bruno, DB Browser for SQLite). First recording
  (~46 min) → **Needs Edits**: narration 64% (reviewer count) vs 70%, typing 46% vs 35%, overlap 268 s.
  Re-record with `Odin_Task2_LibraryAPI_Script.txt/.html` (short ~30-line code, BEFORE/WHILE TYPING
  narration, exact line numbers). Metadata: `Metadata_3kuwe593.rtf`. Original input kept in
  `/Users/Shared/original`.
- Project files live in `C:\Users\uttam\OneDrive\Desktop\nvidia\` (scripts, starter guide).
- Handoff repo (private): https://github.com/uttam12331/odin-handoff - README.md + HANDOFF.md hold the current status; commit SKILL.md changes there.

## Adding new rules
When the user (or a screenshot of Studio / Slack / reviewer feedback) gives a new or changed Odin
rule:
1. Edit this SKILL.md: update the relevant section above in place (replace outdated values).
2. Append one line to the log below: `- YYYY-MM-DD – rule – source`.
3. If it changes an existing script or checklist, say which file should be updated and offer to do it.
4. Tell the user in one line that the skill was updated.

## Rules log
- 2026-10-03 – Writer Guidelines PDF (137 pages) baseline – Downloads
- 2026-10-17 – Ideas proposed in Studio (+ Create Task); AutoQC 2 checks; 4 uploads – onboarding-v3 video
- 2026-10-19 – Idea form = one box with 5 headings; epilogue 3–4 min required; length 15:00–50:59 – Studio
- 2026-10-21 – Hourly pay model; first task $150 + $250 – Studio "Your pay"
- 2026-10-22 – Safari/Chrome allowed; TextEdit banned except Metadata.rtf; avoid desktop Excel – Studio
- 2026-10-23 – TaskRecorder 2.4.4 needs no login; separate Mac user optional – Studio
- 2026-10-26 – Narration counted by reviewer, no coding exception; reading code symbols ≠ narration;
  coding typing limit 35%; overlap max 30 s; use Run full AutoQC after re-record – 3kuwe593 review
- 2026-10-28 – 3kuwe593 second recording: narration fixed but typing 38.02% > 35% (Required finding). Cut typing: run pytest/app with mouse (VS Code Testing panel / Run button), Bruno Clone, DB Browser Filter instead of typed SQL, and add real mouse-driven verification (Bruno PUT/update requests, Runner) – AutoQC check 19
