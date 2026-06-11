# Image Inventory & Manifest — what's actually in Supabase

Source of truth: bucket **`LISA WOOD STUDIO WEBSITE`** (public) in Supabase project
`SURFACE SURVEYS` (`aawnkxnnrymqbysgimqj`). Audited 2026-06-11 by querying
`storage.objects` directly. Pages fetch these **in-browser at runtime** from the
public URL base:

```
https://aawnkxnnrymqbysgimqj.supabase.co/storage/v1/object/public/LISA%20WOOD%20STUDIO%20WEBSITE/
```

## Three findings that shape the build

1. **Installations are MULTIMEDIA.** Real video/audio in the folders:
   - Attention → `ATTENTION by LISA WOOD STUDIO_Proxy.mp3` (audio)
   - ECS → `ECS 24 ANIMATION.mp4` (video) — only 2 files total
   - Mind the Gap → `MTG.mp4`, `MTG ANI 24.mp4` (video)
   - Winterblue → entire `WINTERBLUE VIDEO/` (14 files)
   → The **Installation** page model needs video/audio sections, not just stills.

2. **Each project hides a curated subfolder among working files.** Target the curated
   one, ignore raw/working dirs (`BLUE`, `Media`, `SEARCH`, `search images`).

3. **Filenames don't encode curatorial order** (except Side Effects `1–4.jpg`). Omani is
   full of color variants of the same shot. → **Hero + order is a curation choice**, made
   by the agent or Lisa — exactly like section order.

## Per-project manifest (recommended canonical folder)

| Project | Discipline | Recommended folder | Files | Media | Notes / decision |
|---|---|---|---|---|---|
| **Surface Surveys** | Photographs | `surface-surveys/` | 168 | images | **2 versions exist.** Kebab-case has all **6 chapters** (city, craters, greenland, simpson-desert, wahiba-oman, white-sands) + web-slug names. Uppercase `SURFACE SURVEYS/` has only 5 (no Craters). → use kebab. *Confirm.* |
| **Omani Landscapes** | Photographs | `OMANI LANDSCAPES/` | 32 | images | Flat. Many color variants of same shots → needs curation/hero pick. |
| **Winterblue** | Photographs | `WINTERBLUE/web-2000px/` | 14 | images (+video) | Web-optimized set. Full set in `/photos` (51). `WINTERBLUE VIDEO/` (14) for a video block. *Confirm web-2000px vs photos.* |
| **Flipped** | Photographs | `flipped/final-photos/` | 57 | images | Clean curated set. Uppercase `FLIPPED/` (BLUE, Media) is working files — ignore. |
| **Palouse** | Photographs | — | 0 | — | **No media yet.** Lisa to add. |
| **Side Effects** | Installation | `SIDE EFFECTS/` | 6 | images | Cleanly numbered `1–4.jpg` + 2 final-artwork PNGs. Best-ordered project. |
| **Attention** | Installation | `ATTENTION/` | 5 | images + **audio** | Front/back of a piece + an `.mp3`. |
| **ECS** | Installation | `ECS/` | 2 | image + **video** | Only 2 files (1 jpg + 1 mp4). Sparse — may need more. |
| **Mind the Gap** | Installation | `MIND THE GAP/` | 6 | images + **video** | 2 `.mp4` + 3 stills. |
| **Luxuriate in Discomfort** | Installation | `LUXURIATE IN DISCOMFORT/photos/` | 6 | images | + `…Show/` (5) + `…Book/` (2). Bespoke page. |

## Decisions needed from Lisa (no rush — captured here)
1. **Surface Surveys:** confirm `surface-surveys/` (kebab, 6 chapters) as canonical?
2. **Winterblue:** web-ready `web-2000px/` (14) or full `photos/` (51)?
3. **Video/audio:** should Installation pages embed the `.mp4`/`.mp3` media? (Likely yes —
   it's core to the work. Affects the Installation section vocabulary.)
4. **Hero + order:** OK for the agent to propose image order + hero (you adjust), since
   filenames don't encode it?

## Next (once folders confirmed)
Bake exact ordered file lists + public URLs into `data/image-manifest.json`, then wire
the browser-side resolver (Phase 4) so a generated page pulls its real photos.
