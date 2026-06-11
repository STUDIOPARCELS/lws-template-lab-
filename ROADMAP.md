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
| 2 | **Scope now** | **Photographs + Installation only.** The other 3 nav disciplines — Writing, Conceptual, Apps — are explicitly OUT for now. |
| 3 | **Bespoke pages** | **Surface Surveys** (Photographs; 6 chapters) + **Luxuriate in Discomfort** (Installation) are the homepage-featured bodies → **unique hand-crafted pages**, not the generator. |
| 4 | **Section selection** | Canonical *set* of sections per discipline; **skip-if-empty**; **order is design-driven, not fixed.** |
| 5 | **Images** | **One Supabase folder per project**; pages auto-pull that folder's images in order (browser-side). |
| 6 | **Deploy / approval** | **sandbox branch → Vercel preview → Lisa approves → promote to `main` (production).** No more direct-to-production. |
| 7 | **First loop** | **Design polish first** — perfect the spatial system, spacing, and typography of the template library *before* wiring automation. |

### Why "agent chooses order" matters
Greenland's opening hero should not feel identical to Craters' or to an installation's.
Same building blocks, different composition — the agent reads each project's content
and sequences sections for editorial impact. This is the core differentiator.

### Ground truth from planning
- **SSOT covers 8 entries** (Surface Surveys + its 6 chapters, Omani Landscapes) with full
  content. **8 roster projects have NO SSOT entry yet**: Winterblue, Flipped, Palouse
  (Photographs) + Side Effects, Attention, ECS, Mind the Gap, Luxuriate in Discomfort
  (Installation). Content must come from Lisa — Claude never invents narratives.
- **Claude now has direct Supabase access** (MCP) — bucket/folder structure is verified
  ground truth, not assumption. Pages still fetch images **in-browser** at runtime from
  the public bucket; visual confirmation stays with Lisa on the sandbox preview.
- **Templates already bind SSOT data** — the generator extends existing work, not a rewrite.

---

## Project roster (locked 2026-06-11, per Lisa)

| Discipline | Projects | Supabase folder status |
|---|---|---|
| **Photographs** | Surface Surveys (collection, 6 chapters) · Omani Landscapes · Winterblue · Flipped · Palouse · **21st Century in Black & White** *(added 06-11)* | Image folders locked in `data/image-manifest.json`. Palouse media not yet uploaded. |
| **Installation** | Side Effects · Attention · ECS · Mind the Gap · Luxuriate in Discomfort (**collection**, 3 sub-projects incl. LUX Public Art) | All have media; ECS sparse (2 files). |

**Out (Writing discipline, not now):** Lost Vibrations, Time of Becoming. **LUX Public Art** is a child of Luxuriate, not separate.

## Content decisions & data (2026-06-11, per Lisa — apply at merge)
| Project | Year | Medium / equipment | Location |
|---|---|---|---|
| Flipped | 2023–2026 | Generative AI + Leica medium-format | **Ilulissat Icefjord, Greenland** (UNESCO World Heritage Site) — two expeditions |
| Winterblue | 2023–2025 | Leica S (Typ 007) + iPhone Pro Max | — |
| Palouse | 2013 | Nikon D800 | — |

- **Description sections:** DEFERRED — decide only after *all* narrative content is in and confirmed.
- **CTA:** button label = "Inquire" (all). But the **post-click action differs by discipline** (Installation vs Photographs vs Conceptual) — wire per-discipline later.
- **Title display:** store clean title case in SSOT; render ALL-CAPS via one CSS rule (matches the live site, e.g. "SURFACE SURVEYS").
- **Image/folder architecture:** delegated to Claude → locked in `data/image-manifest.json` (manifest is the single source of truth; non-destructive; one folder per project/child).
- **Still open (non-blocking, proceeding on these defaults unless corrected):** Attention "from 200" → "2001"; Mind the Gap display title ("Mind the Gap" vs source "MIND | FIND THE GAP") + dimension typo (`26ft W`); Palouse 60×40&quot; print dims.

- **Viceroy: removed — not part of this site.**
- **Writing / Conceptual / Apps:** nav links exist but disciplines are untouched for now.
- Media source of truth: bucket **`LISA WOOD STUDIO WEBSITE`** (public) in Supabase
  project `SURFACE SURVEYS` (`aawnkxnnrymqbysgimqj`), one folder per project.
  Ignore the flat `make-e667ad39-images` bucket (legacy automation dump).

### Navigation concept (directional, not final design)
- Header: `LISA WOOD STUDIO` left · `PHOTOGRAPHS  WRITING  INSTALLATION  CONCEPTUAL  APPS` right
- **About** lives on the homepage (not in the main nav)
- **`SUN VALLEY, IDAHO`** corner tag (placement to be refined)
- Homepage features **Surface Surveys + Luxuriate in Discomfort** only (no Winterblue there)

## Disciplines & the section vocabulary (scope now)

**Photographs** and **Installation** share this section vocabulary (the agent picks
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
- ✅ Word-boundary text truncation (no more mid-word cuts) — shipped to sandbox.
- ✅ Canonical 8/92 page margin enforced; drifters snapped. **Deliberate choices
  preserved**: grid-8's doubled padding (Lisa's request), full-bleed images at 0/100.
- Next: vertical rhythm + typography spacing within the SSOT (Inter + Space Mono, no serif).
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
