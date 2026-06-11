# HANDOFF PROMPT — paste into a NEW Claude Code session (Fable 5)

> **How to launch (PowerShell):**
> ```
> cd "D:\LWS\OBSERVATORY FINAL\WEBSITE\WEBSITE FOLDERS"
> claude --model claude-fable-5
> ```
> Then paste everything in the block below. Starting LOCALLY matters: the missing
> renderer code is most likely in this folder.

```
You are picking up Lisa Wood Studio's website/template system. Read fully before acting.
A prior cloud session wasted effort in the wrong system — these findings are VERIFIED, trust them.

═══ MISSION ═══
Lisa already designed and saved ~78 filled template sections. Recover their renderer,
assemble them into project pages, show Lisa rendered pages on a sandbox preview, iterate,
and promote to production only on her approval. NEVER invent templates or freestyle HTML.

═══ VERIFIED SYSTEM MAP (2026-06-11) ═══
• Lisa's REAL templates = a SLOT-BASED system. 78 rows in Supabase table `lws_template_pages`
  (project ref `aawnkxnnrymqbysgimqj`, "SURFACE SURVEYS" project, org STUDIO PARCELS).
  Saved 2026-05-23 → 05-30 across 2 drafts. 10 template kinds:
  project-hero · project-desktop · brand-splash · blackout-desktop · landscape-hero ·
  split-hero · triptych · detail-grid · detail-grid-single-row · analysis-poster-pair
  Each row: template_id, project_slug, sort_order, placement(hero|body), reveal(fade|up),
  text_slots[] {slotId,label,value,style{role,weight},visible},
  image_slots[] {slotId,label,fullSrc,assetSrc(/render/image/ transform),storagePath,
                 crop{x,y},transform{flipX,flipY},visible}.
  A page = all rows for one project_slug ordered by sort_order. EVERYTHING needed to
  rebuild pages is in these rows EXCEPT the layout code per template kind.
• templatelab.lisawoodstudio.com = Vercel project `lws-template-lab` = GitHub repo
  STUDIOPARCELS/lws-template-lab- (main). That app is a NEWER canvas tool (13 hardcoded
  absolute-position templates, saves to `lws_cloud_workspace`) — it is NOT the slot system
  and did NOT write the 78 rows. Do not confuse them.
• THE MISSING PIECE: the slot renderer (layout code for the 10 kinds). It is NOT in the
  lws-template-lab repo, NOT in observatory.lisawoodstudio.com HTML, NOT in lisa-wood-studio's
  HTML shell. STRONG LEAD: this local archive contains `template-lab/`, `template-lab-current/`,
  and `TEMPLATE PAGES EXAMPLES/` folders. Also possible: a Figma Make app (the
  `make-e667ad39-images` bucket + `kv_store_e667ad39` table suggest one existed).
• Slot images were uploaded to bucket "LISA WOOD STUDIO WEBSITE" under
  `template-lab/<project>/<template-id>/<slotId>/<timestamp>-<file>`.
• `lws_project_content` (18 rows) = canonical project SSOT (narrative_description, years,
  location, medium, all 5 *_description fields, artwork_atoms, cta...).
• Content intake already done: branch `content/local-intake` in the GitHub repo (verbatim
  extractions from this archive + INTAKE-REPORT.md). Confirmed facts: installations all 2022;
  Flipped 2023–2026 (Ilulissat Icefjord, generative AI + Leica); Winterblue 2023 Camas Prairie
  (125-photo contact sheet, Leica S007 + iPhone); Palouse 2013 Nikon D800; Luxuriate =
  umbrella + 3 children (book, one-night installation, LUX public art); 21st Century in
  Black & White = Installation; disciplines in scope = Photographs + Installation only.

═══ FIRST MOVES (in order) ═══
1. INVENTORY this folder for the slot renderer: look in `template-lab-current/`, `template-lab/`,
   `TEMPLATE PAGES EXAMPLES/` for code containing `text_slots` / `image_slots` / `project-hero` /
   `lws_template_pages`. Report what each folder contains BEFORE changing anything.
2. Show Lisa what you found; confirm which is the canonical renderer.
3. Render ONE page from the real data: pull White Sands' 8 rows from `lws_template_pages`
   (Supabase MCP or REST with her anon key) → render through the recovered renderer →
   save HTML → show Lisa.
4. If (and only if) no renderer exists anywhere: rebuild the 10 layouts faithfully from
   Lisa's screenshots/examples, one at a time, with her sign-off per template.
5. Then: assemble all projects' pages, deploy to the sandbox (repo branch `sandbox/claude`
   → Vercel preview), Lisa approves → promote to production.

═══ RULES (cost was paid for these) ═══
1. Lisa's saved work in `lws_template_pages` is the source of truth. Query it; don't assume.
2. Render templates EXACTLY as designed — recover the real renderer before any rebuilding.
3. Never push to `main`/production without Lisa's explicit approval (sandbox preview first).
4. Show Lisa RENDERED PAGES (files/URLs she can open) — never just tables or descriptions.
5. Her voice: never rewrite her narratives; verbatim or flagged-for-review only.
```
