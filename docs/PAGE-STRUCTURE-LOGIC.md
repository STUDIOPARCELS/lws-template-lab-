# Project Page Structure — the template logic (LWS)

The architecture for how each project page is composed. This is the design thinking from
the planning session; the section below maps it onto the REAL slot templates that already
exist in the engine (so it's buildable, not abstract).

## 1. Core principle — "shared vocabulary, agent-chosen order"
A **discipline** (Photographs, Installation) shares the **same vocabulary of section types**.
But the **order of sections is chosen per project by design judgment** — NOT one fixed recipe.
So Greenland opens differently from Craters, which opens differently from an installation.
**Variation by design intelligence is the whole point** — pages feel composed, not stamped.

## 2. The section vocabulary (the building blocks)
Abstract role → the REAL slot templates that realize it (in `lws_template_pages`):

| Section role | Job | Real slot template(s) |
|---|---|---|
| **Hero / opening** | the entry image + title | `project-hero`, `landscape-hero`, `split-hero`, `blackout-desktop` |
| **Survey / brand splash** | title + location + dates over imagery | `brand-splash` |
| **Narrative / intro** | the story + metadata rows (DATE / LOCATION / EQUIPMENT / MEDIA) | `project-hero` (body+meta), `project-desktop` |
| **Image study** | sequences & grids of the work | `triptych`, `detail-grid`, `detail-grid-single-row` |
| **Analysis / plate** | paired images with analysis | `analysis-poster-pair` |
| **Media (video/audio)** | installation film/sound | ⚠️ GAP — not built yet; installations need it |

## 3. Per-discipline page structure
**Photographs** (Surface Surveys chapters, Omani, Winterblue, Flipped, Palouse):
  Hero → Narrative/intro (with metadata rows) → Image study (triptych / grids) → close.
  Image-rich; the photographs are the star.

**Installation** (Side Effects, Attention, ECS, Mind the Gap, 21st Century, Luxuriate):
  Hero → Narrative/concept → **Media (video/audio)** → physical specs (scale: "49ft × 15ft") →
  fewer images. Concept-led; needs the Media section built.

## 4. The composition rules
- **Skip-if-empty** — a section only appears if its content exists. No empty shells.
- **Agent-ordered** — the section ORDER varies per project (the differentiator). The engine's
  **`/project-section-organizer`** is exactly this mechanism — evaluate/use it, don't rebuild.
- **Title displays ALL-CAPS**; **CTA label = "Inquire"** everywhere (post-click differs per
  discipline, later).
- **Lisa's narrative voice is sacred** — verbatim or flagged-for-review; never invented.

## 5. Bespoke collections (NOT the generic generator)
- **Surface Surveys** — a collection of **6 chapters** (Greenland, White Sands, Wahiba,
  Craters, Simpson Desert, City of Rocks). Its own collection page + per-chapter pages.
- **Luxuriate in Discomfort** — an umbrella over **3 children** (the book, the one-night
  "December, Sun Valley" installation, and LUX public art). Its own collection page.
- These are multi-year / multi-dimensional, so they get hand-crafted structure, then the
  same section vocabulary inside each chapter/child.

## 6. Images
- **One Supabase folder per project** (manifest maps id → folder).
- **Hero image + order are a curation choice** (filenames don't encode order) — the agent
  proposes, Lisa confirms. Web-optimized via the `/render/image/` transform.

## 7. How this maps to the real engine (important)
The 10 slot templates **ARE** this vocabulary — Lisa already built them. The
`/project-section-organizer` route **is** the "agent chooses order per project" mechanism.
So this logic is already half-realized in `lisa-wood-studio`: the job is to (a) make sure
every project has the right sections saved, (b) let the organizer order them, (c) build the
missing Media section for installations, and (d) render/approve/ship. Compose ONLY from these
real templates — never freestyle.
