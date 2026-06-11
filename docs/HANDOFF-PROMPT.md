# HANDOFF PROMPT — paste into a new Claude Code (Fable 5) session

> Copy everything in the code block below into a fresh session that is set to
> **Fable 5** (`/model claude-fable-5`). It carries the full state + the hard-won
> corrections so the new session starts in the RIGHT system instead of re-deriving it.

```
You are picking up Lisa Wood Studio's website build. Use model Fable 5. Read this in full
before doing anything — a prior session wasted effort in the wrong system; do not repeat it.

═══ MISSION ═══
Assemble Lisa's ALREADY-CREATED templates into finished project pages, review them on a
sandbox preview, and (on her approval) promote to production. You are not inventing
templates or writing freestyle HTML/CSS. Lisa designed the templates already.

═══ THE REAL SYSTEM (this is the correction that matters) ═══
Lisa's templates are a SLOT-BASED system — NOT absolute-positioned layers, NOT the
hardcoded templates in the `lws-template-lab` repo (that repo is an OLDER tool — ignore its
13 templates, its demo-flipped.html, its review/ sheets, its scripts/fill_sections.py).

The real template LAYOUTS (project-hero, brand-splash, etc.) are defined in code that is
NOT in lws-template-lab — almost certainly the **lisa-wood-studio** Next.js project/repo.
FIRST STEP: ask Lisa which repo/Vercel project renders the slot templates, and work there.

The 10 template kinds Lisa has built (in Supabase `lws_template_pages`):
  project-hero · project-desktop · brand-splash · blackout-desktop · landscape-hero
  split-hero · triptych · detail-grid · detail-grid-single-row · analysis-poster-pair

═══ DATA SOURCES (Supabase, via MCP — project ref `aawnkxnnrymqbysgimqj`, "SURFACE SURVEYS") ═══
• `lws_template_pages` (78 rows) = Lisa's SAVED, FILLED templates. THE source of truth.
   cols: id, slug, page_title, project_slug, project_title, template_id, template_title,
         status, sort_order, placement (hero|body), reveal (fade|up),
         image_slots (jsonb[]), text_slots (jsonb[]), layers (jsonb, usually {}).
   text_slots[]  = {slotId, label, value, style:{role,weight}, visible}
   image_slots[] = {slotId, label, fullSrc, assetSrc (often a /render/image/ transform URL
                    ?width=2000&quality=86&resize=contain), storagePath, crop:{x,y},
                    transform:{flipX,flipY}, mediaType, visible}
   A page = all rows for one project_slug, ordered by sort_order, placement hero then body.
• `lws_project_content` (18 rows) = the canonical SSOT the website reads.
   cols incl: slug, title, page_type, parent, narrative_description, years, location,
   medium, process, dimensions, edition, cta, scientific/visual/geographic/atmospheric/
   spatial_description, poetic_words, ethereal_description, artwork_atoms, field_images_path.
• `lws_cloud_workspace` (1 row) = the lab's synced savedSections blob (legacy).
• Storage bucket "LISA WOOD STUDIO WEBSITE" (public) = all media, one folder per project.
   Real paths are nested, e.g. `surface-surveys/white-sands/photos/full-res/...` and
   `flipped/final-photos/web-2000px/...`. Web-optimized via the /render/image/ transform.

═══ WHAT TO IGNORE in lws-template-lab repo (prior session's detours) ═══
demo-flipped.html (freestyle — wrong), review/*.html + scripts/fill_sections.py (rendered the
OLD hardcoded templates — wrong), the 13 loadTemplate defaults in index.html. The repo's
data/ssot-projects.json (19 entries, merged from a content intake) PARALLELS
lws_project_content — reconcile, don't assume it's what the site uses. data/image-manifest.json
has the image folder map but its paths are too shallow (real ones are nested — see above).

═══ USEFUL, REAL WORK already done (keep) ═══
• Content intake from Lisa's local archive → branch `content/local-intake` (8+ project JSONs
  + report). Verbatim transcriptions, flags for studio-drafted bits.
• Confirmed facts: installations all 2022; Flipped 2023–2026 (Ilulissat Icefjord, generative
  AI + Leica); Winterblue 2023 Camas Prairie (125-photo contact sheet, Leica S007 + iPhone);
  Palouse 2013 Nikon D800; Luxuriate = umbrella + 3 children (book, one-night install, LUX
  public art); 21st Century in Black & White = Installation; Lost Vibrations + Time of
  Becoming = Writing (out of scope). Photographs + Installation are the only disciplines now.

═══ DEPLOY / APPROVAL GATE (do not break) ═══
Work on branch `sandbox/claude` (mirror to `claude/loving-bell-7ruOQ`). NEVER push to `main`
(production) without Lisa's explicit approval. Vercel auto-previews the branch; Lisa reviews
the preview URL, approves, then you promote sandbox→main. Show her RENDERED pages (send files
or give preview URLs) — she works visually; tables/prose are not enough.

═══ RULES (learned the hard way) ═══
1. Compose ONLY from Lisa's actual created templates (the slot system). Never freestyle.
2. Render each template EXACTLY as Lisa designed it — use the real renderer, not a lookalike.
3. lws_template_pages is the truth for "what Lisa made." When unsure, query it, don't assume.

═══ FIRST MOVES ═══
1. Confirm with Lisa: which repo/Vercel project is the slot-template renderer (lisa-wood-studio?).
2. In that system, pull a project's rows from lws_template_pages and render them with the REAL
   renderer → one finished page (start with White Sands: 8 templates, fully filled).
3. Send Lisa the rendered page. Iterate from her feedback. Then scale to all projects.
```
