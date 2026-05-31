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

## Deploy & Develop (GitHub + Vercel — Recommended Workflow)

The goal is that **your GitHub repo is the single source of truth**.  
You edit locally → `git add` + `git commit` + `git push` → Vercel automatically updates the live site.

### Current Recommended Setup

1. Your code lives in this folder.
2. It is connected to this GitHub repo (the single source of truth):  
   `https://github.com/STUDIOPARCELS/lws-template-lab-`
3. Vercel should be connected to the same repo with **Production Branch = `main`**.
4. Every `git push origin main` will trigger a new production deployment on Vercel.

**Latest commit on GitHub right now:** `b59a844` (Docs update for Git-first workflow) — this is confirmed as the top commit.

### How to Make Changes Going Forward (Git Flow)

```powershell
# 1. Make your edits to the files (index.html, CSS, JS, data, etc.)

# 2. Commit and push
git add .
git commit -m "Your description of the change"
git push origin main
```

A few seconds later, Vercel will automatically build and deploy the new version.

### If You See a 403 / "Authentication Required" / Login Screen Instead of Your Site (Most Common)

If visiting your `.vercel.app` URL shows **"Authentication Required"**, a **Vercel login screen**, or a **403 Forbidden** error, your site is actually fine and fully deployed — it is just locked behind **Vercel Authentication** (a.k.a. Deployment Protection). Team projects turn this **ON by default**, so only people who are logged into your Vercel team can see the site. Everyone else (and you, in an incognito window) gets a 403.

**Fix — makes the site publicly visible, ~30 seconds:**
1. Open your project: https://vercel.com/lisa-woods-projects-87a1cfaa/lws-template-lab
2. Go to **Settings** → **Deployment Protection**.
3. Under **Vercel Authentication**, switch it to **Disabled** (Off).
4. Click **Save**.
5. Reload your site URL in a private/incognito window — it now loads for everyone.

This only controls *who is allowed to view* the deployed site. Your build and GitHub connection are unaffected.

### If the Live Site is Not Updating After a Push

The GitHub → Vercel connection auto-deploys every push to `main`. If a change does not appear:
1. Make sure your local changes are committed **and** pushed: `git push origin main`. (Running `vercel --prod` from an uncommitted local folder can publish a different version than what is on GitHub.)
2. Check the latest deployment at the project URL above — it should say **Ready**.
3. Hard-refresh your browser (Ctrl/Cmd + Shift + R) to bypass cache.

> Deleting and re-importing the Vercel project is almost never necessary, and it will **not** fix a 403/login wall — that is the Deployment Protection setting above, not the Git connection.

See [DEPLOYMENT.md](./DEPLOYMENT.md) for more details.

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
