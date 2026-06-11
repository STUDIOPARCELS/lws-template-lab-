# LWS Template Lab — Roadmap to a Self-Composing Site

> **North Star:** Add a project to the SSOT → a complete, on-brand page composes
> itself, where an **AI agent uses design judgment to choose the section order**
> for that specific project. It arrives as a **draft on a sandbox preview** that
> Lisa approves, then promotes to production (GitHub → Vercel; images from Supabase).
> The template editor becomes the **design vocabulary** the agent composes with.

This file is the single source of truth for *where we're going and why*. Decisions
below are **locked** unless we deliberately revisit them.

---

## Locked Decisions (planning, 2026-06)

| # | Decision | Choice |
|---|----------|--------|
| 1 | **Page model** | **Discipline-based shared structure.** A discipline (e.g. Photography, Installation) shares the *same vocabulary of section types* — but the **agent chooses the section ORDER per project** using design expertise, so each project opens differently. |
| 2 | **Scope now** | **Photography + Installation only.** Conceptual / Apps / Writing get their own unique page languages later. |
| 3 | **Bespoke pages** | **Surface Surveys** and **Luxuriate in Discomfort** are multi-year, multi-dimensional bodies of work with sub-projects → **unique hand-crafted pages**, not the disciplinary generator. |
| 4 | **Section selection** | Canonical *set* of sections per discipline; **skip-if-empty**; **order is design-driven, not fixed.** |
| 5 | **Images** | **One Supabase folder per project**; pages auto-pull that folder's images in order (browser-side). |
| 6 | **Deploy / approval** | **sandbox branch → Vercel preview → Lisa approves → promote to `main` (production).** No more direct-to-production. |
| 7 | **First loop** | **Design polish first** — perfect the spatial system, spacing, and typography of the template library *before* wiring automation. |

### Why "agent chooses order" matters
Greenland's opening hero should not feel identical to Craters' or to an installation's.
Same building blocks, different composition — the agent reads each project's content
and sequences sections for editorial impact. This is the core differentiator.

### Ground truth from planning
- **SSOT is complete** for all 8 current projects (narrative, year, location, all 5
  description sections, all 3 artwork atoms). Generated pages will be rich; skip-if-empty
  is a safety net, not a common case.
- **Build sandbox can't reach Supabase** (network policy); the **browser can**. So image
  auto-pull and any live-image verification happen in-browser, confirmed visually with Lisa.
- **Templates already bind SSOT data** — the generator extends existing work, not a rewrite.

---

## Disciplines & the section vocabulary (scope now)

**Photography** and **Installation** share this section vocabulary (the agent picks
which to use and in what order, per project):

- Hero (full-image / full-bleed / split) — *the opening; varies per project*
- Narrative / Editorial — the `narrative` body
- Specifications — `medium`, `process`, `edition`, artwork atoms
- Description Sections — scientific / visual / geographic / atmospheric / spatial
- Image study — grid-8 / grid-4 / triptych / duo
- Quote / CTA close — `cta`

**Bespoke (own pages):** Surface Surveys, Luxuriate in Discomfort.
**Future disciplines (own languages):** Conceptual, Apps, Writing.

---

## Architecture

```
SSOT (data/ssot-projects.json)
   │            ┌───────────────────────────────────────────┐
   ▼            │  DESIGN SYSTEM (polished spatial grid +    │
 PROJECT  ──►   │  .lws-* type roles) ← Phase 1 hardens this │
   │            └───────────────────────────────────────────┘
   ▼
 DISCIPLINE → section vocabulary (which sections are eligible)
   │
   ▼
 AGENT COMPOSER → chooses ORDER per project (design judgment) → ordered sections
   │
   ▼
 IMAGE RESOLVER (project → Supabase folder → images in order)
   │
   ▼
 DRAFT in Page Builder → Lisa reviews/tweaks
   │
   ▼
 PUBLISH → sandbox branch → Vercel preview → APPROVE → promote to main
```

---

## Phased Plan (each phase ships to sandbox, green, Lisa-approved)

### ✅ Phase 0 — Plan & lock *(this document)*

### ▶ Phase 1 — Design polish (FIRST LOOP, current)
Establish a **shared spatial system** and apply it across the whole template library:
- Canonical **page margins**, **column grid**, and **vertical rhythm** (so any section
  order still aligns edge-to-edge — the foundation that makes agent-reordering look
  intentional, not random).
- Fix inconsistencies (e.g. grid uses 23% outer margin vs 8% elsewhere; crude
  `substring()` text truncation; ad-hoc vertical positions).
- Tighten typography spacing within the SSOT (Inter + Space Mono, no serif).
- **Outcome:** a beautiful, internally-consistent template library — the design
  language the agent will later compose with.

### Phase 2 — Discipline structure + section vocabulary
Encode the Photography/Installation section vocabulary as data; build the eligibility
+ skip-if-empty logic. **Outcome:** the system knows what sections a project *can* have.

### Phase 3 — Agent composer (design-driven order) → draft
"✨ Generate Draft" → agent sequences sections per project → full draft in Page Builder.
**Outcome:** one project, auto-composed with a thoughtfully chosen order, text bound,
smart image placeholders.

### Phase 4 — Image auto-pull (folder per project)
Resolve project → Supabase folder; auto-fill slots in order; hybrid placeholder fallback.
**Outcome:** drafts arrive with real photos.

### Phase 5 — Bespoke pages
Hand-craft Surface Surveys + Luxuriate in Discomfort (sub-project structure).

### Phase 6 — Approve→promote loop + agent skill
Per-section regenerate/swap; one-button promote sandbox→production; package as a
Claude Code **agent skill** so "add a project" → draft appears for approval.

---

## How we work (the loop)
1. Build the smallest shippable slice of the current phase.
2. Push to **sandbox** → Lisa previews on the Vercel preview URL.
3. Refine → commit → push. Promote to **main** only on Lisa's approval.
4. Update this file whenever a decision changes. Phase done when green + approved.

Constraints that never change: two-font SSOT (Inter + Space Mono, **no serif**),
equal section padding, `.lws-*` typography roles.
