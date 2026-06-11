# Content Intake Report — 8 Projects

Local content extraction for the Lisa Wood Studio website SSOT. Source: local archive at
`D:\LWS\OBSERVATORY FINAL\WEBSITE\WEBSITE FOLDERS`. Eight project JSONs were created in
`content-intake/` using the SSOT schema. Nothing in `data/ssot-projects.json`, `index.html`, or
any other repo file was touched.

**Method note:** All text was extracted directly from the source documents with `python-docx` /
`pypdf` and written to JSON in UTF-8, so Lisa's exact characters (em-dashes, curly apostrophes)
are preserved. Only Lisa's own words were used — no paraphrasing, no invented copy. Empty fields
are intentional and flagged below as gaps.

**`descriptionSections` (scientific / visual / geographic / atmospheric / spatial) were left empty
for all 8 projects.** In the existing SSOT (Surface Surveys, Omani Landscapes) these are short
editorial keyword distillations, not verbatim source text. Faithful intake can't manufacture them;
they should be composed in the cloud session from the `narrative` content. Flagged per project.

---

## 1. Folder → Project mapping

| Project (brief)          | Folder                          | Text content found | Intake file |
|--------------------------|---------------------------------|--------------------|-------------|
| Winterblue (photo)       | `WINTERBLUE/`                   | **None** (media only) | `winterblue.json` |
| Flipped (photo)          | `FLIPPED/`                      | Yes (.docx ×7)     | `flipped.json` |
| Palouse (photo)          | `PALOUSE/`                      | **None** (media only) | `palouse.json` |
| Side Effects (install)   | `SIDE EFFECTS/`                 | Yes (.docx)        | `side-effects.json` |
| Attention (install)      | `ATTENTION/`                    | Yes (.docx)        | `attention.json` |
| ECS (install)            | `ECS/`                          | Yes (.docx)        | `ecs.json` |
| Mind the Gap (install)   | `MIND THE GAP/`                 | Yes (.docx)        | `mind-the-gap.json` |
| Luxuriate in Discomfort  | `LUXURIATE IN DISCOMFORT/`      | Yes (.docx, .pdf, .txt) | `luxuriate-in-discomfort.json` |

### Unmatched folders (NOT part of this intake — reported for awareness)

These top-level folders exist in the archive but are not among the 8 requested projects:

- `SURFACE SURVEYS/` — existing SSOT entry. **New material present** (see "New material" below). Not modified.
- `OMANI LANDSCAPES/` — existing SSOT entry. **New material present** (see below). Not modified.
- `21st Century in Black & White/` — separate project (`21st Century in Black and White.docx` + images). Not requested.
- `Totems & Sentinels/` — separate project (`Totems _ Sentinels.docx` + images). Not requested.
- `LOST VIBRATIONS/` — large research/white-paper body (canine shaking, fast-twitch muscle vibrations). Not a website project folder per the brief.
- `TIME OF BECOMING Book Series/` — children's book project (`How Dog Got Vision`). Not requested.
- `MICRON HOUSE/` — only a stub `.txt` (a URL). Not requested.
- `HOW TO FALL COURSE/`, `SOLOKIT/` — non-art-project material.
- `SSOT AND DESIGN/` — design system + SSOT reference docs (`SSOT FOR PROJECT PAGES.docx`, `LWS-design-system_FINAL.docx`, `SSOt.txt`). Reference only.
- `TEMPLATE PAGES EXAMPLES/`, `template-lab/`, `template-lab-current/` — website template/working copies; `template-lab*/data/ssot-projects.json` is the existing SSOT (used here only as a read-only schema reference).

---

## 2. Per-project: fields filled, sources, and gaps

### winterblue — `_confidence: thin`
- **Filled:** id, title (`Winterblue`), type, parent. Nothing else.
- **Sources:** none (no `.docx`/`.pdf`/`.txt`/`.md`/`.rtf` anywhere in `WINTERBLUE/` or elsewhere in the archive).
- **GAPS (all content):** narrative, year, location, medium, process, edition, cta, all descriptionSections, all artworkAtoms. **Needs Lisa to supply the narrative and all metadata.**
- Media present that hints at scope: `WINTERBLUE.mp4`, `WINTERBLUE I_1.mp4`, audio `Winterblue_First_Storm_LWS_1.mp3`, `WINTERBLUE I PRINT THUMB.jpg`, `WB COLLAGE 2 copy.jpg`, plus a `Media/photos/` shoot set and a `Media/search images/` set.

### flipped — `_confidence: assembled-from-fragments`
- **Filled:** narrative (Logline + Concept + synthesis paragraph, verbatim from `FLIPPED.docx`); medium (`Large format photographs (Leica Medium Format + AI Generated)`, from Master Production Document); process (Method + Materials lines, verbatim); location (`Greenland (source photographs)` — see note).
- **Sources:** `FLIPPED/Content/FLIPPED.docx`, `FLIPPED/Content/MASTER PRODUCTION DOCUMENT_Flipped.docx`.
- **GAPS:** year (no year stated in docs); edition (docs only say "Edition strategy can remain tight" — no concrete edition); cta; all descriptionSections; artworkAtoms.material / printer / dimensions (Deliverables mention "Large archival prints", a diptych "Tilt/Resolve", a triptych "Before/Flip/After", and an optional silent gallery loop — these are *form*, not concrete print specs).
- **Ambiguous / for Lisa:** `location` was set to "Greenland (source photographs)" because the docs repeatedly name Greenland as the photographic source; confirm whether that's the right value for a work that pairs Greenland medium-format with AI-generated imagery. Other `FLIPPED/Content/` docs were **not** extracted (marketing/business — see §4).

### palouse — `_confidence: thin`
- **Filled:** id, title (`Palouse`), type, parent. Nothing else.
- **Sources:** none (no text documents; only `.claude/settings.local.json`).
- **GAPS (all content):** narrative, year, location, medium, process, edition, cta, all descriptionSections, all artworkAtoms. **Needs Lisa to supply everything.**
- **Note for Lisa:** several filenames encode print sizes — `No 12 60X40 inches.jpg`, `No13 60X40 inches.jpg`, `No14 60X40 inches.jpg` — suggesting 60×40 inch prints. This was **not** written into `dimensions` (filename ≠ stated spec); confirm if you want it used.

### side-effects — `_confidence: verbatim`
- **Filled:** narrative (5 statement paragraphs, verbatim); year (`2022`); medium (`Two Text Murals`); artworkAtoms.dimensions (`Two Wall Murals - 49ft W X 15ft H`).
- **Sources:** `SIDE EFFECTS/Content/SIDE EFFECTS.docx`.
- **GAPS:** location, process, edition, cta, all descriptionSections, artworkAtoms.material / printer.

### attention — `_confidence: verbatim`
- **Filled:** narrative (5 paragraphs, verbatim); year (`2022`); medium (`Gramophone + Mp3 Audio - 5:09 min`); artworkAtoms.material (`Acrylic, aluminum, stainless steel`); artworkAtoms.dimensions (`Gramophone: 6.25 sq ft X 6.85 ft H; Wall Text Decal: 30ft W X 22ft H; Mp3 Audio: 5:09 min`).
- **Sources:** `ATTENTION/Content/ATTENTION.docx`.
- **GAPS:** location, process, edition, cta, all descriptionSections, artworkAtoms.printer.
- **Ambiguous / for Lisa:** the doc says queries start "from 200" — almost certainly a typo for **2001** (the same paragraph later says "in 2001, Google released top keyword search data"). Left verbatim in the source; not altered.

### ecs — `_confidence: verbatim`
- **Filled:** narrative (3 paragraphs, verbatim; the wrapped cannabinoid-system sentence rejoined); year (`2021`); medium (`LED Screen, Animated Text`); artworkAtoms.dimensions (`LED Screen: 13ft W X 4ft H X 3.5in D`).
- **Sources:** `ECS/Content/ECS.docx`.
- **GAPS:** location, process, edition, cta, all descriptionSections, artworkAtoms.material / printer.

### mind-the-gap — `_confidence: verbatim`
- **Filled:** narrative (T.S. Eliot epigraph + the "directs our attention" stanza, verbatim); year (`2022`); medium (`Animated Neon`); artworkAtoms.dimensions (`NEON: 15ft W X 26ft W X 4ft H`).
- **Sources:** `MIND THE GAP/Content/MIND THE GAP.docx`.
- **GAPS:** location, process, edition, cta, all descriptionSections, artworkAtoms.material / printer.
- **Ambiguous / for Lisa:**
  - **Title:** the document is titled `MIND | FIND THE GAP` (with the pipe and the word "FIND"), but the project/folder is "Mind the Gap." The verbatim doc title was kept in `title`. Confirm the intended display title.
  - **Dimensions typo:** source reads `15ft W X 26ft W X 4ft H` — two "W" values (the second is likely meant to be L or H). Left verbatim; confirm.

### luxuriate-in-discomfort — `_confidence: assembled-from-fragments`
- **Filled:** narrative (4 statement paragraphs, verbatim from the installation `.docx`); year (`2018 – 2020`); medium (`Multimedia Installation`); location (`Sun Valley, Idaho`, from the Installation Statement PDF: "December, 2020 I Sun Valley, Idaho"); artworkAtoms.material (`Stainless Steel`); artworkAtoms.dimensions (full component list: LUX Sculpture, two vending machines, neon, HEAT & COLD poems, book).
- **Sources:** `…/Luxuriate in Discomfort.docx`, `…/Installation Statement - Luxuriating In Discomfort (2).pdf`, `…/Luxuriate in Discomfort NARRARIVE.txt`.
- **GAPS:** process, edition, cta, all descriptionSections, artworkAtoms.printer.
- **Additional verbatim material available (NOT folded into fields — for Lisa/cloud review):**
  - The **Installation Statement PDF** contains a richer first-person statement (the July 1 2018 origin, the "year painting," HEAT/COLD poem descriptions, the Andy Goldsworthy *Leaning into the Wind* video note). Only `location` was drawn from it; the rest could enrich the narrative if desired.
  - The **book** `luxuriate in discomfort book lws.pdf` (14 pages) is the full poem/aphorism text of the book itself.
  - **LUX Public Art** is a *separate, related extension* (a public-art proposal on the young-adult mental-health crisis): `LUX.docx` (brand identity / marketing), `LUX Public Art overview.pdf` (paradox / practice / gesture / origin-story text, partly AI-assistant dialogue). These were **not** used for the installation entry. If LUX Public Art should be its own SSOT project, flag it — it has its own statement text and images.

---

## 3. Files that could not be read

- `LUXURIATE IN DISCOMFORT/LUX Public Art/Content/LUX 2025.pdf` — **not extracted (276 MB).** Too large to process safely; almost certainly an image-heavy presentation/deck. Needs Lisa's eyes or a targeted extraction if its text matters.
- No other text files failed. `python-docx` and `pypdf` read all `.docx`/`.pdf`/`.txt` for the 8 projects without error. (No `.pages` or `.rtf` files exist for these projects.)

---

## 4. Present but intentionally NOT extracted (non-narrative / business)

In `FLIPPED/Content/` (confirmed by reading their opening text — all marketing/ops, not artist statement):
- `MARKETING PLAN FLIPPED.docx`, `MARKETING STRUCTURE FLIPPED.docx` — marketing strategy.
- `TRANSACTION IMPLEMENTATION FLIPPED.docx` — WooCommerce/Stripe/Xero/WLT automation plan.
- `You are correct.docx` — an AI-assistant chat transcript (studioparcels analysis), not creative content.
- `FLIPPED NARRATIVE NOTES.docx` — a long ChatGPT brainstorm transcript exploring 50-photo sequences; **read in full**, but it is process/ideation, not a finished statement, so nothing was lifted verbatim into fields.

The `supabase-*-map.json` files in several `Media/` folders are upload manifests, not content.

---

## 5. Anything ambiguous that needs Lisa's eyes (summary)

1. **Winterblue & Palouse have no written content at all** — both need narrative, year, location, medium, edition, etc. supplied from scratch.
2. **`descriptionSections` are empty for all 8** by design — they need cloud-side editorial distillation from each narrative (matching the Surface Surveys / Omani style).
3. **`cta` left empty for all 8** — existing entries use `"Inquire"`; apply the site convention in the cloud session if desired.
4. **Flipped:** no year in any document; confirm. `location` = "Greenland (source photographs)" needs confirming.
5. **Attention:** "from 200" is a likely typo for "2001."
6. **Mind the Gap:** display title (`MIND | FIND THE GAP` vs "Mind the Gap") and the `26ft W` dimension typo.
7. **Luxuriate:** decide whether to enrich the narrative from the Installation Statement PDF / book, and whether **LUX Public Art** should become its own separate SSOT project.

---

## 6. New material for EXISTING entries (report only — not modified)

- **Surface Surveys** (`SURFACE SURVEYS/`): contains additional documents beyond what's in the SSOT — `SURFACE SURVEYS PROJECT NARRATIVE.docx`, `SURVAFE SURVEYS PROJECT.docx`, `LISA WOOD STUDIO Surface Surveys Brief.docx`, `A VEILED SANTUARY ESSAY.docx` (a White Sands essay), a `README..txt`, and per-chapter `supabase-full-res-map.json` photo maps (City, Craters, Greenland, Simpson Desert, White Sands, Wahiba Oman). Possible source for richer chapter text if you want to expand existing entries.
- **Omani Landscapes** (`OMANI LANDSCAPES/`): `Content/LAYOUTS/VIDEO_ASSETS/LOST_VIBRATIONS_VIDEO_IMAGE_PROMPTS.md` and `…_EXAGGERATED.md` (video/image prompt scripts), plus `DERIVED BENTO TILES/*__bento-crops.json` and a `supabase-full-res-map.json`. Mostly production assets, not new narrative.

---

## 7. Image inventory per project (filenames only — for Supabase cross-checking)

Web derivatives (`web-2000px/…`) omitted; those mirror the originals listed here.

### winterblue
- Hero/media: `WB COLLAGE 2 copy.jpg`, `WINTERBLUE I PRINT THUMB.jpg`, `WINTERBLUE.mp4`, `WINTERBLUE I_1.mp4`, `Winterblue_First_Storm_LWS_1.mp3`
- `Media/photos/`: `1_Proxy_2.jpg`, `1.22.23 (10).JPEG`, `2_Proxy_3.jpg`, `2.JPEG`, `8.JPEG`, `9.JPEG`, `File_006.png`, `IMG_0584 copy.jpg`, `IMG_0822.JPEG`, `IMG_4512.JPEG`, `IMG_4857.JPEG`, `IMG_4962 copy.jpg`, `IMG_4962.HEIC`, `IMG_5766_Proxy_1 copy.jpg`, `IMG_5767_Proxy.jpg`, `IMG_5882.JPEG`, `IMG_5951.JPEG`, `IMG_5952.JPEG`, `IMG_5974.JPEG`, `IMG_6263_Proxy.png`, `IMG_6363.JPEG`, `IMG_7405.JPEG`, `IMG_7456.JPEG`, `IMG_8313.JPEG`, `IMG_9070.JPEG`
- `Media/search images/`: `IMG_4008.JPEG`, `IMG_4016.JPEG`, `IMG_4026.JPEG`, `IMG_4042.JPEG`

### flipped
Final set — `FLIPPED/Media/FINAL PHOTOS/`:
- `1.png`, `1 ZOOM.webp`, `1 SUPER ZOOM.png`, `2.png`, `2 ZOOM.webp`, `3.png`, `3 zoom .webp`, `4.png`, `4 ZOOM.webp`, `5.png`, `5 ZOOM.png`, `6.png`, `6 zoom.webp`, `ZOOM.webp`, `iceberg10 copy.webp`
- AI-generated finals: `ChatGPT Image May 20, 2026, 02_40_40 PM.png`, `Gemini_Generated_Image_nbtz0rnbtz0rnbtz (1).jpg`, and five `lisawoodstudio_…mj.run….webp/png` files.
- (Large `Media/ALL IMAGES_OLD/` archive — BLUE/ and WHITE/ ORIGINALS, plus `processed-webp/flipped-01…22` and `flipped-blue-01…12` — is prior/working material; ~230 images total in the folder.)

### palouse
- Named prints: `No 12 60X40 inches.jpg`, `No 28.jpg`, `No 36.jpg`, `No13 60X40 inches.jpg`, `No14 60X40 inches.jpg`, `Road 4.jpg`, `WIP 008 PRINT.jpg`, `WIP 028.psb`, `WIP 044.jpg`
- 55 raw scans `_DSC0015.jpg … _DSC9846.jpg` (each duplicated as a `(1)` copy).

### side-effects
- `SIDE EFFECTS/Media/`: `1.jpg`, `2.jpg`, `3.jpg`, `4.jpg`

### attention
- `ATTENTION/Media/ORIGINALS/`: `ATT BACK  copy.jpg`, `ATTENTION copy.webp`, `ATTN 24 c3.jpg`, `front again copy (1).jpg`, `ATTENTION by LISA WOOD STUDIO_Proxy.mp3`, `ATTENTIONTEXT FINAL_Proxy.mp4`, `ATTN SPEECH TO TEXT_Proxy.mp4`

### ecs
- `ECS/Media/ORIGINALS/`: `ecs 3 copy 2.jpg`, `ECS 24 ANIMATION.mp4` (plus web derivative `ecs 3 copy 3.webp`)

### mind-the-gap
- `MIND THE GAP/Media/`: `ani 1.jpg`, `f copy.jpg`, `mind.jpg`, `MTG FRONT copy.jpg`, `MTG ANI 24.mp4`, `MTG.mp4`

### luxuriate-in-discomfort
- One Night Installation `photos/`: `BOOKS AND MIRROR.jpg`, `L1009804.jpg`, `L1009809.jpg`, `L1009902 copy.webp`, `L1009908.jpg`, `L1009938 book in mirrorRE copy.jpg`, `L1009942 LID blur mirror.jpg`
- Poems: `COLD POEM.jpg`, `HEAT POEM copy 2.jpg`
- Book: `LUXURIATE IN DISCOMFORT BOOK/` — `BOOK ZOOM.webp`, `L1009908.jpg`, `L1009938 book in mirrorRE copy.jpg`, and `pages/page-01…28.webp` (28-page scan + `_contact-sheet.jpg`)
- LUX Public Art `ORIGINALS/` (related extension): `back 3.png`, `COLD POEM.jpg`, `HEAT POEM copy 2.jpg`, `jp.jpg`, `PUB ART.webp`, `PUB ART2.webp`, and four `ChatGPT Image May 17, 2026…png` renders.
