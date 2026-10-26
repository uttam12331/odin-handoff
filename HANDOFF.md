# Handoff: where we stopped

Last updated: 2026-10-26.

## Status at a glance

| Task | What | Status | Next step |
|---|---|---|---|
| **3kuwe593** | Library API validation (Visual Studio Code, Bruno, DB Browser for SQLite) | **Needs Edits**. Second recording just finished, not uploaded yet | Check the video → replace 3 files → **Run full AutoQC** → submit |
| **veiw1b03** | Q3 returns analysis (DBeaver, VS Code, Google Sheets) | Approved, **on hold** | Waiting for Maven to fix the OTA password (Google Sheets needs it) |
| nkjsf88f | Empty Idea Draft created by mistake | Ignore | Never submit it |

## Next step (task 3kuwe593)

The second recording has been made. Do these in order, all in the recording Mac user (**[REC.MAC]**):

1. **Check the recording.** In TaskRecorder (status **Idle**) → **Show Recordings** → newest
   `recording_…` folder → play `video.mp4`:
   - length must be 15:00–50:59
   - clear picture and audible narration
   - only VS Code on screen during the epilogue
   - screenshots folder count must be more than 0.5 × the video length in seconds
2. **Delete the old files from the Desktop**: the old `video.mp4`, `recording_….zip` and
   `deliverables.zip`.
3. **Copy the new files** with Option-drag (makes a copy):
   - the newest `recording_….zip`. **Never create or rename it.**
   - `video.mp4` from the newest folder
4. **Make the new deliverables.zip:**
   - delete `__pycache__` and `.pytest_cache` from `Desktop/LibraryAPI` (Cmd+Shift+. shows hidden files)
   - create a `deliverables` folder containing:
     - `input 1/`: app.py + requirements.txt from `/Users/Shared/original` (same as `code-start/`)
     - `final output 1/`: the whole `Desktop/LibraryAPI` folder, including the **Library API QA** Bruno collection
   - right-click → **Compress**
5. **Studio → task 3kuwe593 → Upload task files:**
   - replace **Screen recording (MP4)**, **Task Recorder zip** and **Deliverables.zip**
   - keep the existing **Metadata.rtf** (same as `tasks/3kuwe593-library-api/Metadata.rtf`)
   - **Save Changes**
6. **Run full AutoQC** in check 1, **not** "Rerun failing". Check 2 (narration) runs by itself about
   10 minutes later. Targets:

   | Check | Target |
   |---|---|
   | Narration (#24) | at least **70%** of actions state what/where/why |
   | Typing (#19) | at most **35%** |
   | Window overlap (#17) | at most **30 s** |

7. **Update the form and submit:**
   - update Resolution, Light/Dark and "UI element changed" if they differ from last time
   - re-tick the manual checks honestly against the **new** video (tick typing only if it's within the limit)
   - Final note:
     ```
     Re-recorded after review feedback: narration now states what, where (line numbers, panels) and why for each step instead of reading code aloud; typing reduced; inactive apps minimized to avoid window overlap. The starting Flask project (input 1) was AI-generated with Gemini before recording.
     ```
   - tick the final confirmation → **Submit for Review**
8. If it comes back as **Needs Edits** again, copy the Review Feedback and reviewer notes into Claude.

## Why the first recording of 3kuwe593 failed

AutoQC and the reviewer flagged three problems:

- **Narration was 50.6% by AutoQC, 64% by the reviewer's count.** The minimum is 70%.
  - Code was read aloud symbol by symbol ("def isbn underscore ok bracket…"), which counts as no what/where/why.
  - The edits at 26:33–28:30 weren't narrated.
  - The reviewer said: "The guidelines have no coding exception."
- **Typing was 45.96%.** The limit for coding tasks is 35%. About 100 lines were typed slowly, and VS Code's
  "Screen Reader Optimized" mode was on, which turned off autocomplete.
- **Window overlap lasted 268 s** (41:37–46:05). DB Browser stayed open behind VS Code.

The disputes on all three were rejected, so the task came back as Needs Edits. Here's what the second recording does differently:

| Fix | How |
|---|---|
| Shorter code | About 30 typed lines instead of about 100: one `check()` function, copy and paste of our own lines, and one pytest test with a loop |
| Narration that counts | A **BEFORE** line before each code block (what + line number + why) and a **WHILE TYPING** line in plain English, never symbols |
| No overlap | Minimize each app before opening the next; only VS Code is on screen during the epilogue |
| Faster typing | "Screen Reader Optimized" turned off and Tab autocomplete used |

## Facts about task 3kuwe593

- **Approved Goal.** Paste it exactly, typos included, into the Goal PDF, the TaskRecorder Task
  Description and the Metadata Request:
  ```
  I will make the API more reliable for the QA team and also add input validation to the create book and update book endpoints. I will validate required fields, ISBN-13 format and checksum ,publication year and page count. I will also make sure the API returns proper JSON error messages with the correct HTTP status codes such as 400, 404, and 409, and write a pytest file containing tests for them.
  ```
- **TaskRecorder Used Apps:** `Visual Studio Code`, `Bruno`, `DB Browser for SQLite`
- **Starting input:** `code-start/app.py`, 75 lines, made with Gemini, with fictional authors and
  valid ISBNs. Running it once creates `books.db` with 8 books.
- **Finished code:** `code-final/`. It's tested: pytest passes and the API returns
  201 / 409 / 400 / 404 correctly.
- **Python on the Mac:** use the venv `~/venvs/analysis/bin/python`. Homebrew Python 3.15 blocks pip.
- **Bruno:** the request type is HTTP. Set the Body to JSON. Assert is under the `>>` tab overflow.
  Use `http`, not `https`.

## Mac setup used

- Recording user: **rec.mac**. Studio, Slack and Metadata are kept in the main user.
- Dock on the right, clock with seconds, Accessibility Inspector running (dot), Do Not Disturb on.
- The wallpaper, or another UI element, is changed for every recording.
- Insightful: sign in with @mercor.expert, Odin → Play, keep it minimized.

## Common problems we hit

| Problem | Fix |
|---|---|
| "Paste" doesn't work in Finder's sidebar "Shared" | Use Go → Go to Folder → `/Users/Shared`. The sidebar entry is the network one |
| TaskRecorder asks to sign in | It's an old version. Install 2.4.4 from World files |
| VS Code menu bar missing | The window is in Full Screen. Use green button → Fill |
| pytest `assert 400 == 409` / `500 == 201` | Look for typos: `' isbn'` with a space, `isn` instead of `isbn`, the year in quotes, or the file not saved (dot on the tab) |
| DB Browser query "shows nothing" | Correct. 0 rows means no duplicates |
| Bruno 415 error | The Body isn't set to JSON |
