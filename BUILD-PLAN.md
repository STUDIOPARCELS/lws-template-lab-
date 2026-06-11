# Build Plan — Templates → Confirmed Sections → AI-Assembled Pages

**The contract (Lisa, 2026-06-11):** The 13 template-lab sections are THE building
blocks — already designed, already tuned. The pipeline is:

```
1. FILL      every template section with each project's real SSOT text
2. CONFIRM   Lisa reviews the filled sections (review sheets on sandbox) ✓/edit
3. ASSEMBLE  the AI organizes ONLY confirmed sections into pages (order varies per project)
4. SEE       Lisa reviews pages → feedback → learn → regenerate → approve → production
```

**Rule #1 (Learnings Log, from Lisa):** Pages are composed FROM the template-lab
sections — exact geometry, exact `.lws-*` type roles, the lab's own export pipeline
(`buildComposedPageHTML`: equal-padding fit, 1280×720 canvas math). **Never freestyle
HTML/CSS.** (`demo-flipped.html` violated this — kept only as the lesson.)

---

## To-do

### Stage A — FILL: the writing goes INTO the templates
- [x] **A1** `scripts/fill_sections.py` — transcribes the 13 template definitions
      exactly from `index.html` (`loadTemplate`), binds every project's SSOT content,
      extracts the `.lws-*` CSS verbatim from the lab → `data/filled-sections.json`
- [x] **A2** **Section Review Sheets** — `review/<project>.html`: every template
      section filled with that project's real text, rendered with the lab's own
      export math. Real images wired where unambiguous (flipped, side-effects);
      lab-style placeholders elsewhere. + `review/index.html` directory.
- [ ] **A3** Lisa reviews on sandbox → per section: ✓ confirm / comment / kill.
      Edits applied → regenerate → repeat until confirmed per project.

### Stage B — ASSEMBLE: AI organizes confirmed sections into pages
- [ ] **B1** `confirmed-sections.json` = the contract (only ✓ sections enter pages)
- [ ] **B2** Composer stacks confirmed sections per project — **section order chosen
      per project** (the agent's design judgment; varies, never one fixed recipe),
      via the lab's `buildComposedPageHTML` logic → `pages/<project>.html`
- [ ] **B3** Image slots auto-filled from `data/image-manifest.json` folders

### Stage C — SEE: pages on the preview → recursive improvement
- [ ] **C1** All pages on sandbox preview + index
- [ ] **C2** Lisa's page feedback → Learnings Log rules → regenerate (each pass better)
- [ ] **C3** Approved → promote `sandbox/claude` → `main` (production)

### Stage D — LOCK: repeatability
- [ ] **D1** "Add a project → filled sections → confirm → page" packaged as the
      one-command skill, documented in this repo

---

## Learnings Log
| # | From | Rule |
|---|------|------|
| 1 | Lisa, on demo-flipped | Compose ONLY from template-lab sections (geometry + `.lws-*` + lab export math). Never freestyle. |
