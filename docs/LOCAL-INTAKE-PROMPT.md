# Local Content Intake — prompt for a Claude Code instance on Lisa's machine

**How to use (Windows):**
1. Install Claude Code if needed: `npm install -g @anthropic-ai/claude-code` (or use the desktop app)
2. Open PowerShell and run:
   ```
   cd "D:\LWS\OBSERVATORY FINAL\WEBSITE\WEBSITE FOLDERS"
   claude
   ```
3. Paste the entire prompt below. When it finishes and pushes, come back to the cloud
   session and say "intake is pushed."

---

## THE PROMPT (copy everything below this line)

You are doing CONTENT EXTRACTION for Lisa Wood Studio's website SSOT. Your job is to
read, organize, and faithfully transcribe — **NEVER to invent, embellish, or paraphrase
creative content**. If information doesn't exist in the files, leave the field as ""
and log it as a gap. Lisa's voice is the product; preserve her exact wording.

### Context
The website repo is `studioparcels/lws-template-lab-` on GitHub. Its single source of
truth is `data/ssot-projects.json`. It already contains complete entries for Surface
Surveys (and its 6 chapters) and Omani Landscapes. EIGHT projects need entries, and the
content lives in the folders around you:

- **Photographs:** Winterblue, Flipped, Palouse
- **Installation:** Side Effects, Attention, ECS, Mind the Gap, Luxuriate in Discomfort

### Step 1 — Inventory
Recursively list this directory. Produce a tree of folders/files with sizes. Identify
which folders correspond to which of the 8 projects (names may vary in case/spelling).
Also note any folders with NEW material for the existing Surface Surveys / Omani
Landscapes entries — report only, don't modify those.

### Step 2 — Read everything relevant
Read every text-bearing file for the 8 projects: .docx, .pdf, .txt, .md, .rtf, .pages
if possible. For .docx use python-docx (pip install python-docx); for .pdf use pypdf
or pdfplumber. If a file can't be read, log it — do not guess its contents.
Note image files (names + counts) but do not upload them.

### Step 3 — Extract into SSOT schema
For each of the 8 projects create `content-intake/<project-id>.json` (kebab-case id,
e.g. `winterblue`, `side-effects`) with EXACTLY this schema:

```json
{
  "id": "",
  "title": "",
  "type": "photography | installation",
  "parent": "Photography | Installation",
  "narrative": "",
  "year": "",
  "location": "",
  "medium": "",
  "process": "",
  "edition": "",
  "cta": "",
  "descriptionSections": {
    "scientific": "",
    "visual": "",
    "geographic": "",
    "atmospheric": "",
    "spatial": ""
  },
  "artworkAtoms": {
    "material": "",
    "printer": "",
    "dimensions": ""
  },
  "_sources": ["relative/path/to/file-used.docx"],
  "_confidence": "verbatim | assembled-from-fragments | thin"
}
```

Rules:
- **Verbatim first.** Use Lisa's sentences as written. Light cleanup of typos/spacing only.
- If content for a field is spread across files, assemble it but mark
  `_confidence: "assembled-from-fragments"` and list all sources.
- **Empty is correct** when nothing exists. Never fill a field with plausible-sounding
  text. No summaries written in your own voice.
- Where a document clearly maps to a description section (scientific/visual/geographic/
  atmospheric/spatial), place it there; if unclear, put it in narrative and flag it.

### Step 4 — Report
Write `content-intake/INTAKE-REPORT.md`:
- Folder→project mapping table (including unmatched folders)
- Per project: which fields are filled, from which files, and ALL GAPS
- Files you couldn't read
- Anything ambiguous that needs Lisa's eyes
- Image inventory per project (filenames only) for later Supabase cross-checking

### Step 5 — Deliver via GitHub
- Clone `https://github.com/studioparcels/lws-template-lab-.git` to a temp location
  (or ~/lws-intake). If auth is needed, walk Lisa through `gh auth login`.
- Create branch **`content/local-intake`** from `main`.
- Add ONLY the `content-intake/` directory (the 8 JSONs + report). Do NOT touch
  `data/ssot-projects.json`, `index.html`, or any other file.
- Commit: "Content intake: extracted SSOT content for 8 projects from local archives"
- Push the branch: `git push -u origin content/local-intake`
- Do NOT open a pull request. Do NOT push to main or to any sandbox/* branch.

### Final output to Lisa
Show her: the project→fields-filled table, the gaps list, and confirmation of the
pushed branch. Tell her to return to her cloud Claude session and say "intake is pushed."
