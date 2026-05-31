# LWS Template Lab

**Visual Section Layout Editor + Page Builder** for Lisa Wood Studio.

Single source of truth (SSOT) driven. Text-first. Built exactly to your design system and project content (Surface Surveys chapters + Omani Landscapes).

## What It Is
- 1280px standard desktop canvas with rule-of-thirds + center guides + layer-to-layer snapping
- 8+ design templates including the exact "Full Image Hero" (16:6 ratio, ~30% height, minimal metadata + description in lower-right with padding) you specified
- Drag layers, 4-corner resize handles on images, double-click text to edit inline
- Strict typography role assignment using the real `.lws-*` classes from your design system
- Quick Text palette that inserts correctly-mapped fields (project-title-h1, narrative-description-body, description-section-*, metadata-*, artwork-atom-*, etc.)
- Full undo (Ctrl/Cmd+Z), Reset Layout, Reset All, New Blank Canvas
- **Page Builder**: save sections, reorder, export multi-section production HTML pages
- One-click clean self-contained HTML exports that use your real `lws-type-system.css`
- Prominent **Download Full Backup** + Import (never lose work)
- **Live Supabase image browser** — paste your anon key once, then click 🖼️ Browse Supabase Images to load real photos from your bucket and insert them directly into any template (Full Image Hero, Split, Editorial, etc.). Real public URLs are used in all exports.

## Quick Start (Local)

1. Open `index.html` directly in any modern browser (Chrome/Firefox/Edge recommended).
2. Select a project (Greenland, White Sands, Wahiba, Craters, Simpson Desert, City of Rocks, Omani Landscapes, etc.).
3. Pick a template or use Quick Text buttons.
4. Drag, resize, edit, delete.
5. Use **Page Builder** to combine sections.
6. **Download Full Backup** frequently.

No build step. No server. Works offline.

## Deploy (GitHub + Vercel — Your Stack)

See [DEPLOYMENT.md](./DEPLOYMENT.md) for the exact commands.

**Fastest path**: Zip this folder → drag to Vercel → instant live URL.

**Proper path** (recommended):
```powershell
cd template-lab
git init
git add .
git commit -m "LWS Template Lab v1"
git remote add origin https://github.com/YOUR_USERNAME/lws-template-lab.git
git push -u origin main
```
Then import the repo in Vercel.

## Supabase (Already Connected)

- Public URL and bucket name are hardcoded.
- Paste your anon key only in the in-app "Supabase Settings" panel when you are ready to browse real images from the "LISA WOOD STUDIO WEBSITE" bucket.
- The key lives only in your browser.

## Data Sources
All project text comes directly from:
- `SSOT AND DESIGN/SSOt.txt`
- `LWS-design-system_FINAL.docx`
- `SSOT FOR PROJECT PAGES.docx`

Typography roles match your canonical system.

## Safety
- Auto-saves to localStorage
- Full JSON backup export (includes everything)
- Isolated folder — never touches other work trees

## Keyboard
- Drag = move
- Corner handles = resize (images especially)
- Double-click text = inline edit
- Delete / Backspace = remove selected layer
- Ctrl/Cmd + Z = undo (20 steps)

---

Built for Lisa Wood Studio. Text-first. SSOT-true. Ready for production pages and future image integration.
