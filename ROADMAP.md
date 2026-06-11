# LWS Template Lab — Roadmap to a Self-Composing Site

> **North Star:** Add a project to the SSOT → a complete, on-brand, multi-section
> page composes itself (right templates, right text, auto-pulled images) as a
> **draft you approve**, then publishes through your existing stack
> (GitHub → Vercel, images from Supabase). The template editor stops being the
> product and becomes the **design vocabulary** the generator speaks.

This file is the single source of truth for *where we're going and why*. We update
it as we go. Decisions below are **locked** unless we deliberately revisit them.

---

## Locked Decisions (from planning, 2026-06)

| # | Decision | Choice |
|---|----------|--------|
| 1 | **End target** | Existing stack: generator outputs clean HTML → committed to GitHub → auto-deployed by Vercel; images sourced from Supabase. |
| 2 | **Page recipe** | One **canonical section order**, **skip-if-empty** (a section is omitted when its SSOT data is absent). |
| 3 | **Images** | **Auto-pull from Supabase** per project (browser-side, since the build sandbox can't reach Supabase). Hybrid fallback to smart placeholders where match confidence is low. |
| 4 | **Automation level** | **Draft, then I approve.** Generation produces a full draft page; Lisa reviews/tweaks, then Publishes. |

### Ground truth discovered during planning
- **SSOT is complete** for all 8 projects: every project has narrative, year,
  location, all 5 description sections (scientific/visual/geographic/atmospheric/spatial),
  and all 3 artwork atoms (material/printer/dimensions). → Generated pages will be
  rich for every project; skip-if-empty is a safety net, not a common case.
- **Project ↔ image mapping is the one open unknown.** Bucket has 3 folders
  (`artwork/`, `SURFACE SURVEYS/`, `OMANI LANDSCAPES/`) but there are 8 projects.
  Surface Surveys is the parent collection; greenland/white-sands/wahiba/craters/
  simpson/city-of-rocks are its 6 chapters; omani-landscapes is separate.
  → The internal folder structure must be resolved in-browser (Phase 2).
- **Templates already bind SSOT data** (title/narrative/sections are injected by
  `loadTemplate`). → The generator is an extension of work already done, not a rewrite.

---

## Architecture (the shape of the thing)

```
SSOT (data/ssot-projects.json)
        │
        ▼
  PAGE RECIPE  ──►  GENERATOR  ──►  draft = ordered list of SECTIONS
 (order + field        │                     │
  bindings +           │                     ▼
  skip rules)          │              PAGE BUILDER (review / reorder / tweak)
                       │                     │
              IMAGE RESOLVER                 ▼
            (project → Supabase          PUBLISH  ──►  HTML → GitHub → Vercel
             folder → first N imgs)
```

- **Recipe** = data, not code: an ordered list of `{ template, bindings, skipIf }`.
- **Generator** = walks the recipe for a project, calls each template's existing
  layer-builder with that project's data, returns saved sections.
- **Image resolver** = per project, finds its Supabase folder, lists images,
  assigns them to image slots; leaves smart placeholders when unsure.
- Everything downstream (Page Builder, Publish) **already exists** — the generator
  feeds into it.

---

## Phased Plan (each phase ends shippable + green)

### ✅ Phase 0 — Plan & lock  *(this document)*
Questions asked, data verified, decisions locked, roadmap written.

### ▶ Phase 1 — Recipe + Generator core  *(text only, no images yet)*
- Define the **canonical recipe** as data (proposed below; Lisa refines).
- Build **`generatePageFromProject(projectId)`**: walks the recipe, produces all
  sections with SSOT text bound and **smart, correctly-sized image placeholders**.
- Implement **skip-if-empty**.
- Add a **"✨ Generate Page"** button: pick a project → full draft page appears in
  the Page Builder, ready to review.
- **Outcome:** one click turns any project into a complete on-brand draft. Testable
  immediately against the pristine SSOT.

### Phase 2 — Image auto-pull
- Resolve **project → Supabase folder** (discovered in-browser; mapping table for
  the tricky ones).
- Auto-assign first N images into each section's slots; **hybrid** fallback to
  placeholders where confidence is low.
- **Outcome:** generated drafts arrive with real photos already in place.

### Phase 3 — The draft → approve → publish loop
- Tighten review UX: per-section **Regenerate**, swap template, nudge, then
  **Publish** (HTML → GitHub → Vercel).
- **Outcome:** the full seamless flow Lisa described, with the approval gate intact.

### Phase 4 — Agent skill (the seamless endgame)
- Package the generator as a Claude Code **agent skill** so "add a project" →
  it runs generation, opens the draft for approval, and on approval publishes.
- **Outcome:** adding a project effectively creates its page.

---

## Proposed canonical recipe (Phase 1 starting point — to refine together)

> Order chosen for editorial rhythm: arrive → orient → read → study → look → close.

1. **Full Image Hero** — hero image + `title`, minimal metadata (`year`, `location`).
2. **Narrative / Editorial** — `narrative` body + `title`.
3. **Specifications** — `medium`, `process`, `edition`, artwork atoms
   (`material`, `printer`, `dimensions`).
4. **Description Sections** — the 5 sections (scientific/visual/geographic/
   atmospheric/spatial) as labeled value blocks. *skip-if-empty per section.*
5. **Image grid** — Grid 8 (2×4) or Grid 4-across, auto-filled in Phase 2.
6. **Quote / CTA close** — `cta` (e.g. "Inquire"), optional testimonial.

*Collection pages (Surface Surveys) may also get a chapter index — TBD in Phase 1.*

---

## How we work (the loop)
1. Build the smallest shippable slice of the current phase.
2. Lisa previews in the real app; gives feedback.
3. Refine → commit → push (auto-deploys). Update this file when decisions change.
4. Phase done when it's green and Lisa signs off → next phase.

Everything stays strictly on the **two-font SSOT** (Inter + Space Mono, no serif),
equal section padding, and the `.lws-*` typography roles already defined.
