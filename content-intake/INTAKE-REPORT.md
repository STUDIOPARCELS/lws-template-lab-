# Content Intake Report — Lisa Wood Studio SSOT

Local content extraction for the website SSOT. Source archive:
`D:\LWS\OBSERVATORY FINAL\WEBSITE\WEBSITE FOLDERS`. JSONs live in `content-intake/`, schema-matched
to `data/ssot-projects.json`. Nothing in `data/ssot-projects.json`, `index.html`, or any other repo
file was touched.

**Method:** Text extracted directly from source documents (`python-docx` / `pypdf`) and from
`observatory.lisawoodstudio.com`, written to JSON in UTF-8 so Lisa's exact characters (em-dashes,
apostrophes) are preserved. Lisa's own words used wherever they exist. Empty fields are intentional
gaps. `_imageDimensions` (pixel size + aspect ratio per final image) was computed with Pillow and
added to each entry.

## What changed in this revision
- **Winterblue** — fully populated from `observatory.lisawoodstudio.com/#winterblue` (it is a **2023** Camas Prairie work, not related to the D800/2013).
- **Palouse** — entry created. No written source existed; narrative is **studio-drafted from research + Lisa's notes and flagged inline** (`[STUDIO-DRAFTED…]`) pending her revision. Factual sections sourced from Palouse research.
- **Flipped** — `year` set to `2023-2026`.
- **`cta` = "Inquire"** applied to all entries (per Lisa).
- **`_imageDimensions`** (pixels + aspect ratio) added to every entry.
- **Luxuriate in Discomfort restructured** into an umbrella + **3 child projects** (book, one-night installation, LUX public art), matching the website and the Surface Surveys collection pattern. The large stainless sculpture / vending machines / neon were **reassigned to LUX** (public art concept), and the painting / poems / book / video to the one-night installation — correcting the earlier single-entry conflation.

## Nikon D800 — confirmed
Lisa asked to confirm the camera existed by her ~2013 Palouse shoot. **Yes:** the Nikon D800 was
announced **Feb 7, 2012** and on sale **late March 2012** — well before 2013. The Palouse archive
filenames use Nikon's default `_DSC####` prefix, corroborating the camera.
Sources: [Nikon news](https://www.nikon.com/company/news/2012/0207_dslr_01/), [Wikipedia: Nikon D800](https://en.wikipedia.org/wiki/Nikon_D800).

## Overall practice tenet (context, from `/#practice`)
Captured for reference (informs tone, especially the discomfort-themed works — Winterblue, Luxuriate):
> "Over the past decade, Lisa has produced 17 projects and more than 200 works across photography,
> mixed media, public installation, text, and essay. The work is built through immersion — repetition,
> duration, and close observation in remote terrain, often alone and under physically demanding conditions."
> Core philosophy: **"exit comfort as a means toward adventure, exploration, and discovery."**

No separate `practice.json` was created (not a project) — flag if you want one.

---

## Entries (11)

| id | title | type | parent | confidence | key gaps |
|----|-------|------|--------|------------|----------|
| winterblue | Winterblue | photography | Photography | assembled | edition of 3, 2 APs; fabrication confirmed (Kodak Glossy / Laumont) |
| flipped | FLIPPED | photography | Photography | assembled | year 2023-2026; edition of 3, 2 APs; physical print dimensions not stated |
| palouse | Palouse | photography | Photography | assembled | narrative studio-drafted & Lisa-approved; fabrication (paper/printer) unspecified |
| side-effects | SIDE EFFECTS | installation | Installation | verbatim | location, process |
| attention | ATTENTION | installation | Installation | verbatim | location; "from 200"→2001 typo |
| ecs | ECS | installation | Installation | verbatim | location, material |
| mind-the-gap | MIND \| FIND THE GAP | installation | Installation | verbatim | title form; "26ft W" dim typo |
| luxuriate-in-discomfort | Luxuriate in Discomfort | installation | Installation | assembled | umbrella; descriptionSections studio-distilled |
| luxuriate-book | Luxuriate in Discomfort (Book) | installation | Luxuriate in Discomfort | assembled | edition |
| luxuriate-installation | December, Sun Valley | installation | Luxuriate in Discomfort | assembled | — |
| lux-public-art | LUX | installation | Luxuriate in Discomfort | assembled | location (concept); fabrication/edition |

`descriptionSections` (scientific/visual/geographic/atmospheric/spatial) are **studio-distilled** for
filled entries (the existing SSOT uses these as editorial keyword phrases, not verbatim text) — review
for voice. They remain empty only where there was nothing to distill.

---

## Per-project notes & gaps

### winterblue — from the live site (verbatim), descriptionSections distilled
Narrative (dog-search origin + contact-sheet structure + practice), year 2023, location Camas Prairie,
medium "Large-scale contact sheet, 125 photographs", process (17 winter trips), material (Kodak Glossy
on painted maple wood), printer (Laumont, NY), dimensions (138" x 85" panel). **Gap:** edition.

### flipped — `year: 2023-2026`, `cta: Inquire`
Narrative/medium/process unchanged (verbatim from `FLIPPED.docx` + Master Production Document).
**Gaps:** edition; physical print dimensions (docs describe form — diptych "Tilt/Resolve", triptych
"Before/Flip/After", silent loop — not concrete sizes). See `_imageDimensions` for source-file pixels.

### palouse — created; narrative STUDIO-DRAFTED (needs Lisa's voice)
- Facts used: subject = farmed Palouse landscape; shot circa 2013 (your recollection — "I think 2013"); Nikon D800.
- The narrative paragraph is composed by the studio from regional research and is **flagged inline** with `[STUDIO-DRAFTED…]`. Please rewrite in your voice or approve.
- `descriptionSections` carry researched facts (loess geology, dryland farming, lentil capital, county geography).
- **Gaps / confirm:** exact shoot year; edition; print fabrication (paper/printer); title; whether 60×40 in (from filenames `No 12/13/14 60X40 inches`) is the intended print size.

### side-effects / attention / ecs / mind-the-gap — `cta: Inquire` added
Verbatim narratives and specs unchanged from the first pass. Outstanding flags: Attention "from 200"
(likely 2001); Mind the Gap title `MIND | FIND THE GAP` vs "Mind the Gap" and the `26ft W` dimension typo.

### Luxuriate in Discomfort — umbrella + 3 children
- **luxuriate-in-discomfort** (umbrella): the philosophy (2020–2024, eight-year practice) carried across three projects. descriptionSections summarize all three; modalities sauna / cold plunge / whole-body vibration.
- **luxuriate-book** (2020): 30-page digest, 7" square, written for her eldest son; full poem text is in the book PDF.
- **luxuriate-installation** "December, Sun Valley" (2020): one-night bedroom installation — mixed-media painting, HEAT & COLD poems, book, video (Andy Goldsworthy *Leaning into the Wind*). Narrative drawn largely verbatim from the Installation Statement PDF.
- **lux-public-art** "LUX" (2024): public art concept for teen mental health — stainless sculpture, vending machines, neon, AR portal; Paradox / Practice / Gesture structure. Extended PARADOX/PRACTICE/GESTURE and ORIGIN STORY text is in `LUX Public Art overview.pdf` if you want to enrich.
- **Correction:** the 26.5 ft stainless sculpture, vending machines, and neon belong to **LUX**, not the bedroom installation (per the site). Adjust if your intent differs.

---

## Image sizes & aspect ratios
Per-image pixel dimensions and aspect ratios are embedded in each entry's `_imageDimensions` (final /
display images only; `web-2000px` derivatives and the large `ALL IMAGES_OLD` working archive excluded;
Palouse duplicate `(1)` copies excluded). Dominant aspect families:

| project | images measured | dominant aspect ratio(s) | notes |
|---------|-----------------|--------------------------|-------|
| winterblue | 26 | mixed 4:3 and 3:4 (phone/field captures); hero 16:9 & 1.67:1 | component frames of the 125-photo contact sheet; physical panel 138×85" ≈ 1.62:1 |
| flipped | 22 | 2:1, 1.50:1 (3:2), 1:1, ~2.51:1 | finals are panoramic + square AI frames; widest ~2.52:1 |
| palouse | 63 | **3:2 and 2:3** (Nikon D800 native) | `_DSC` raws 3200×4800 / 4800×3200; named prints 3:2; `60X40 inches` files are tiny 504×336 proxies |
| side-effects | 4 | **1:1** (3840×3840) | square mural source tiles |
| attention | 3 | 16:9 + one 1:1 | gramophone/back/text frames |
| ecs | 1 | ~1.78:1 (16:9) | single LED-screen still |
| mind-the-gap | 4 | 16:9 (3840×2160) | neon stills |
| luxuriate-installation | 9 | mixed 2:3 portrait + ~1.5:1; poems 0.85:1 & 1.09:1 | install + poem scans |
| luxuriate-book | 30 | ~1.02:1 (≈ square) page scans | confirms 7" square book |
| lux-public-art | 9 | 1:1 and 5:6 renders; poems as above | concept renders + poems |

---

## Files that could not be read
- `LUXURIATE IN DISCOMFORT/LUX Public Art/Content/LUX 2025.pdf` — **not extracted (276 MB)**, image-heavy deck; needs targeted extraction or your eyes if its text matters.
- All other `.docx`/`.pdf`/`.txt` for these projects read cleanly. No `.pages`/`.rtf` exist for them.

## Present but intentionally NOT extracted (non-narrative / business)
`FLIPPED/Content/`: `MARKETING PLAN`, `MARKETING STRUCTURE`, `TRANSACTION IMPLEMENTATION` (WooCommerce/
Stripe/Xero/WLT automation), `You are correct.docx` (AI chat transcript), `FLIPPED NARRATIVE NOTES.docx`
(ChatGPT brainstorm — read, not lifted). `supabase-*-map.json` are upload manifests.

## Folder → project mapping (full)
| Project | Folder | Text found |
|---|---|---|
| winterblue | `WINTERBLUE/` | none locally — content from website |
| flipped | `FLIPPED/` | .docx ×2 used (+5 business docs) |
| palouse | `PALOUSE/` | none — created from research |
| side-effects | `SIDE EFFECTS/` | .docx |
| attention | `ATTENTION/` | .docx |
| ecs | `ECS/` | .docx |
| mind-the-gap | `MIND THE GAP/` | .docx |
| luxuriate (all 4) | `LUXURIATE IN DISCOMFORT/` | .docx, .pdf, .txt + website |

**Unmatched folders (not requested):** `21st Century in Black & White/`, `Totems & Sentinels/`,
`LOST VIBRATIONS/`, `TIME OF BECOMING Book Series/`, `MICRON HOUSE/`, `HOW TO FALL COURSE/`, `SOLOKIT/`,
`SSOT AND DESIGN/` (reference), `TEMPLATE PAGES EXAMPLES/`, `template-lab*/` (website working copies).

## New material for EXISTING entries (report only — not modified)
- **Surface Surveys** (`SURFACE SURVEYS/`): extra docs — `SURFACE SURVEYS PROJECT NARRATIVE.docx`, `SURVAFE SURVEYS PROJECT.docx`, `LISA WOOD STUDIO Surface Surveys Brief.docx`, `A VEILED SANTUARY ESSAY.docx`, `README..txt`, per-chapter `supabase-full-res-map.json`. Possible source to expand existing chapter text.
- **Omani Landscapes** (`OMANI LANDSCAPES/`): `LOST_VIBRATIONS_VIDEO_IMAGE_PROMPTS.md` (+`_EXAGGERATED`), bento-crop JSONs — mostly production assets.

## Confirmed by Lisa (this revision)
- **Palouse** narrative approved for now; shoot year **2013** confirmed; print size **60 × 40 inches** confirmed and set. Narrative was studio-drafted from research and is Lisa-approved (draft flag removed).
- **Luxuriate split into 4 entries** (umbrella + book + "December, Sun Valley" + LUX) confirmed.
- **All photography editions are identical: `of 3, 2 APs`** — applied to winterblue, flipped, palouse. (Installations carry no edition.)

## Paper / fabrication (confirmed by Lisa)
All photography prints on **archival pigment, Hahnemühle bright white baryta**, fabricated by **Laumont
Photographic, New York** — both fields now set on winterblue, flipped, and palouse. Lisa confirmed they
switched all papers to the Hahnemühle baryta, so the earlier website-stated "Kodak Glossy" for Winterblue
was superseded (its "mounted on painted maple wood" mounting note retained). Printer is the same for all
photographs.

## Visual descriptions (accessibility) — NEW field `visualDescription`
Lisa asked that every **photography** project carry an ethereal prose description of the terrain / subject,
so a blind visitor can picture the image (distinct from the keyword `descriptionSections.visual`). A new
top-level field **`visualDescription`** was added to **winterblue, flipped, palouse**, written after
viewing representative imagery from each project's folder. Per Lisa, the format is **short comma-separated fragments of one, two, or three words** — no uniform
pattern, NOT sentences, NOT abstract art-jargon ("warm minimalism" rejected), no redundant/obvious words
("wet" implied by pools/meltwater/dripping; "cooled lava" obvious; "crusty"/"haloed moon"/"gold horizon"
removed). **Each line must ebb and flow between one-, two-, and three-word fragments — never uniformly
two-word.** The fragment **count varies by project** (6–10). The words **"aerial" and "close" are not used
in any description** (per Lisa); the scale idea is carried by `ambiguous scale` on the collection instead.
Each blends material/color/what-it-resembles with the **scientific fact that grounds it** for a non-seeing
reader. Current set (with per-fragment word-count pattern):
- **surface-surveys** — `ice, sand, lava, gypsum, granite, elemental, ambiguous scale`
- **greenland** — `glacial, ice, meltwater pools, turquoise, cobalt, fine dark lines` (glacial & ice separated; "crevasses"→"fine dark lines")
- **white-sands** — `gypsum, plaster, blinding white, dripping plaster, meringue, soft folds`
- **wahiba** — `Wahiba Sands, golden, quartz, wind ripples, scribed circles, dry`
- **craters** — `basalt, black, rust-red, gold lichen, lime, iron stain, pitted, cracked`
- **simpson** — `red centre, Australia, iron-red, oxblood, trailing vines, vast`
- **city-of-rocks** — `granite, speckled grey, rust-orange, acid-yellow lichen, lime, pockmarked, cracked`
- **omani-landscapes** — `pink, green, feminine, bread browns, earth tones, dissolved landform, form versus function`
- **winterblue** — `midnight blue, indigo, ice blue, monochromatic, snow, wind-carved drifts, moonlight, sub-zero`
- **flipped** — `cinematic, monumental, icebergs, luminous blue-white, looming peaks, black mirror water, backlit, moody, otherworldly, inverted`
- **palouse** — `loess hills, wind-blown silt, rolling, corduroy furrows, green, brown, spare`

**Excluded:** field / documentary / scouting images (people, vehicles, camps, establishing shots) are NOT
artworks and are not described — only the abstract surface/landscape artworks.
**Aerial vs. ground (kept as metadata only, NOT in the descriptions):** Greenland & Simpson = aerial;
Wahiba & City of Rocks = ground-level; White Sands & Craters = both. The scale ambiguity is intentional
but is conveyed without the words "aerial"/"close".

Installations were **not** given `visualDescription` (Lisa scoped this to photography).

**Drafted for ALL photography** after studying multi-image contact sheets of each chapter (not a single
frame). The Surface Surveys collection, its six chapters, and Omani Landscapes are in
**`content-intake/visual-descriptions.json`** (propagation map) for merging into `data/ssot-projects.json`.
All written as concrete blind-accessible descriptors, e.g.:
- **white-sands** — `brilliant chalk-white, like troweled and dripping wet plaster, whipped meringue and cake-frosting peaks, soft folds of melting wax and fresh snow…`
- **simpson** — `deep brick-red and oxblood ground seen straight down from above, threaded with thin wandering vine lines…, like cracked red leather drawn on with fine roots`
- **craters** — `rough volcanic rock in black and charcoal… rusty red crust blotched with mustard-yellow and lime-green lichen… both a boulder up close and scorched ground seen from above`

(Full text for all eight is in `visual-descriptions.json`.)

### Omani Landscapes — enriched entry (NEW, `content-intake/omani-landscapes.json`)
Lisa supplied the concept and a new source folder (`D:\LWS\ALL ARTWORKS\Omani Landscapes`, circa **2024**).
**Concept — form vs. function:** Leica photographs of Oman are stripped in software to their underlying
patterns, then rebuilt into something that no longer looks like a photograph. At the dawn of generative
AI (which can spin up images that *look* like photographs but aren't), these are photographs that *don't*
look like photographs — asking whether a photograph is defined by **form** (what it looks like) or
**function** (how it was made). A full enriched entry was created (narrative studio-drafted from Lisa's
spoken explanation — flagged inline; year 2024; medium = Leica capture + software pattern-extraction;
edition of 3, 2 APs; Hahnemühle baryta / Laumont). This **supersedes the thinner existing
`omani-landscapes` entry** in `data/ssot-projects.json` — merge/replace in the cloud session.

### Cloud-session instructions to propagate into `data/ssot-projects.json`
1. Add a `visualDescription` (string) field to **every photography** project object, copying the values from `content-intake/visual-descriptions.json` (and from `{winterblue,flipped,palouse}.json`).
2. Replace/merge the existing `omani-landscapes` object with `content-intake/omani-landscapes.json` (review the inline `[STUDIO-DRAFTED…]` narrative flag first).
3. Render `visualDescription` as the image `alt`/longdesc for accessibility, and/or a short on-page caption.

## Remaining open items
1. Minor verbatim typos left as-is: Attention "from 200" (likely 2001); Mind the Gap "26ft W".
2. `visualDescription` not yet added to the existing SSOT photography entries (instructions above) — can be drafted on request.
3. Want a standalone **practice** entry from `/#practice`? Not created yet.
