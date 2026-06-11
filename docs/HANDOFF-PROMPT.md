# HANDOFF PROMPT — new Claude Code session (Fable 5)

> **Where to open:** repo **`STUDIOPARCELS/lisa-wood-studio`** (the engine). Branch
> `rescue/unify-20260609` is the latest known-good (deployed 2026-06-09).
> Paste the block below as the first message.

```
You are picking up Lisa Wood Studio's website engine. Read fully before acting.
These findings are VERIFIED (2026-06-11) — trust them, don't re-derive.

═══ MISSION ═══
THIS repo (lisa-wood-studio) is the engine: it renders Lisa's slot-based templates from
Supabase into project pages. Goal: get every project's page composed from her saved
templates, reviewable on a sandbox preview, promoted to production on her approval —
and make "add a project → page appears for approval" a repeatable loop.

═══ VERIFIED SYSTEM MAP ═══
• ENGINE (this repo): Next.js 16. Routes incl. /templates, /template-preview/[...],
  /projects/[slug], /disciplines/[slug], /work/[slug] (~75 pages),
  /project-section-organizer, APIs /api/template-pages, /api/template-pages/project-heroes,
  /api/template-images, /api/template-user-images/[...path].
  Vercel projects: lisa-wood-studio (+ lisa-wood-studio-sandbox for previews). Deployment
  protection (Vercel Auth) is ON — Lisa can view previews in her browser.
• DATA (Supabase "SURFACE SURVEYS", ref aawnkxnnrymqbysgimqj, org STUDIO PARCELS):
  - lws_template_pages (78 rows, saved 2026-05-23→30, drafts: draft-1=53, hero=25) =
    Lisa's filled slot templates. 10 kinds: project-hero, project-desktop, brand-splash,
    blackout-desktop, landscape-hero, split-hero, triptych, detail-grid,
    detail-grid-single-row, analysis-poster-pair. Rows: template_id, project_slug,
    sort_order, placement(hero|body), reveal, text_slots[]{slotId,label,value,style,visible},
    image_slots[]{slotId,fullSrc,assetSrc,storagePath,crop,transform,visible}.
  - lws_project_content (18 rows) = canonical SSOT (narrative_description, years, location,
    medium, process, dimensions, edition, cta, 5 *_description fields, poetic_words,
    ethereal_description, artwork_atoms, field_images_path).
  - Storage bucket "LISA WOOD STUDIO WEBSITE" (public) = all media; slot uploads under
    template-lab/<project>/<template>/<slot>/; project folders incl.
    surface-surveys/<chapter>/photos/full-res, flipped/final-photos/web-2000px,
    WINTERBLUE/, OMANI LANDSCAPES/, SIDE EFFECTS/, ATTENTION/, ECS/, MIND THE GAP/,
    LUXURIATE IN DISCOMFORT/, 21st Century/. PALOUSE has no folder yet.
• RELATED REPOS (context, mostly hands-off):
  - LWS_WEBSITE-sandbox → observatory.lisawoodstudio.com = current LIVE site (older gen).
  - lws-template-lab- = canvas sketch tool @ templatelab.lisawoodstudio.com (superseded) BUT
    holds valuable docs/data on branch sandbox/claude: ROADMAP.md, BUILD-PLAN.md,
    docs/IMAGE-INVENTORY.md, data/ssot-projects.json (19 entries incl. new projects),
    content-intake/ (verbatim local-archive extractions + INTAKE-REPORT.md).
  - LWS_WEBSITE, STUDIO-WEBSITE, observatory-presentation = older generations (confirm, then archive).
  - kohler-*, solokit-*, micron-*, budget-*, mission-control = unrelated ventures. IGNORE.

═══ CONFIRMED CONTENT FACTS (from Lisa, 2026-06-11) ═══
Disciplines in scope: Photographs + Installation ONLY (Writing/Conceptual/Apps later).
Photographs: Surface Surveys (6 chapters; bespoke collection) · Omani Landscapes ·
Winterblue (2023, Camas Prairie, 125-photo contact sheet, Leica S007 + iPhone) ·
Flipped (2023–2026, Ilulissat Icefjord, generative AI + Leica) · Palouse (2013, Nikon D800).
Installation: Side Effects · Attention · ECS · Mind the Gap · 21st Century in Black & White
(ALL 2022) · Luxuriate in Discomfort (2018–2020 umbrella; children: book 2020, one-night
installation "December, Sun Valley" 2020, LUX public art 2024; bespoke collection).
Homepage features Surface Surveys + Luxuriate in Discomfort. About on homepage, not nav.
"SUN VALLEY, IDAHO" corner tag. Titles display ALL-CAPS. CTA label "Inquire" everywhere
(post-click differs per discipline, later). Lisa's narrative voice is sacred: verbatim or
flagged-for-review only.

═══ GAPS TO CLOSE (the actual work) ═══
1. lws_project_content has 18 rows but template coverage is uneven: rich for Surface Surveys
   chapters + Flipped (7-8 templates each); thin (1 row, project-hero only) for winterblue,
   mind-the-gap, luxuriate children, 21st-century. New projects may lack content rows —
   reconcile with lws-template-lab-'s data/ssot-projects.json + content-intake/ (Lisa-approved).
2. Render/QA every project page from existing rows; list which projects need more saved
   templates; let Lisa fill those in her existing tools (or via the organizer).
3. The "agent chooses section order per project" goal: /project-section-organizer exists —
   evaluate it before building anything new.
4. Sandbox→approve→production loop on lisa-wood-studio(-sandbox).

═══ RULES (hard-won) ═══
1. Lisa's saved work (lws_template_pages) is the source of truth — query, never assume.
2. Render templates EXACTLY via this repo's real renderer. NEVER freestyle HTML/CSS.
3. Never deploy to production without Lisa's explicit approval; preview first, always.
4. Show Lisa RENDERED PAGES (URLs/files) — she judges visually, not from tables.
5. Don't touch unrelated repos (kohler/solokit/micron/budget/mission-control).

═══ FIRST MOVES ═══
1. Map this repo: the template components (the 10 kinds), /api/template-pages, the
   section organizer, how /projects/[slug] assembles rows.
2. Show Lisa /templates and /projects/white-sands on the current preview — confirm this IS
   the system she remembers building (May 23–30).
3. Then execute the gap list above with her, one approved slice at a time.
```
