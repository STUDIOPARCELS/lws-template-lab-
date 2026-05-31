# LWS Template Lab — GitHub + Vercel + Supabase Deployment Guide

This folder (`template-lab/`) is a **completely self-contained**, zero-dependency static tool. It works perfectly when opened directly as `index.html`, dragged to Vercel, or served from GitHub Pages.

## Your Stack (Exactly as Requested)
- **GitHub** (source of truth + version history)
- **Vercel** (instant free hosting + custom domains later)
- **Supabase** (already pre-wired — public URL + bucket filled; anon key via UI only)

---

## 1. Quickest Path: Deploy to Vercel RIGHT NOW (No Git Needed)

1. Zip this entire `template-lab` folder (or just drag the folder).
2. Go to https://vercel.com
3. Sign in with GitHub (recommended) or email.
4. Click **"Add New Project"** → **"Import Git Repository"** (or use the "Upload" drag-and-drop if you don't want Git yet).
5. Drag the whole `template-lab` folder (or the zip) onto the screen.
6. Vercel detects it is a static site. Click **Deploy**.
7. Done. You now have a permanent URL like `https://lws-template-lab-xxx.vercel.app`

**Every future drag of an updated zip will create a new production deployment.**

---

## 2. Recommended Long-Term Workflow: GitHub as Source of Truth + Vercel Auto-Deploy

You want all changes to go through Git. This is the correct setup:

- Edit files locally in this folder.
- `git add .`, `git commit`, `git push origin main`
- Vercel automatically deploys the new version to production.

### Initial One-Time Setup (Already Partially Done)

Your GitHub repo is: https://github.com/STUDIOPARCELS/lws-template-lab-

### Most Common Issue: Site Shows a 403 / Login Screen (Vercel Authentication)

If your `.vercel.app` URL shows **"Authentication Required"**, a **Vercel login page**, or **403 Forbidden**, the deployment is healthy — it is just protected. Vercel **team** projects enable **Vercel Authentication** (Deployment Protection) by default, so only members logged into your team can view the site; the public gets a 403.

**Fix (makes it public, ~30 seconds):**

1. Open the project → **Settings** → **Deployment Protection**.
2. Set **Vercel Authentication** to **Disabled**.
3. Click **Save**, then reload your URL in an incognito window.

> Tip: you can also create a temporary share link from the project's deployment page to preview a protected site without disabling protection.

### Normal Git Workflow (Everything Through GitHub)

```powershell
# Make changes, then:
git add .
git commit -m "Describe your change"
git push origin main
```

Vercel automatically builds and updates the live site within ~30-60 seconds of each push to `main`.

If a push does not show up, confirm it actually reached GitHub (`git push origin main`) and that the newest deployment reads **Ready**. Avoid `vercel --prod` from an uncommitted local folder — it can publish a version that differs from GitHub.

> Deleting and re-importing the project is a last resort only. It does **not** fix a 403/login wall (that is the Deployment Protection setting above) and it discards your project settings and any custom domains.

---

## 3. Supabase Connection (Everything Is Pre-Connected)

All public values are already hard-coded in the app:

- **Project URL**: `https://aawnkxnnrymqbysgimqj.supabase.co`
- **Storage Bucket**: `LISA WOOD STUDIO WEBSITE`

### How to activate image browsing later
1. Open the deployed site (or local `index.html`)
2. Click **"Supabase Settings"** button in the toolbar
3. Paste your **anon public key** (from Supabase Dashboard → Project Settings → API → `anon` `public` key)
4. Click **Save Key** + **Test Connection**
5. The key is stored only in your browser's localStorage — never committed to Git.

> The anon key is **safe to expose** for a public bucket with proper RLS policies. Never paste the `service_role` key here.

**Image browsing is now fully active.** Paste your anon key in the in-app Settings panel, then use the orange **🖼️ Browse Supabase Images** button. It supports your common prefixes (Greenland, White Sands, Wahiba, Omani, etc.) and inserts real hosted images into templates. All exports use the live Supabase public URLs.

---

## 4. Daily Safety Workflow (Never Lose Work)

- The app **auto-saves** to browser localStorage every ~25s.
- **Always** use the big green **⬇ Download Full Backup (Safe)** button before closing the tab or switching projects.
- The backup JSON contains: current canvas, all saved sections, current project, and the full SSOT data.
- Import the backup on any machine via the **Import Backup** button.

---

## 5. What Gets Deployed

Everything inside `template-lab/` is production-ready:
- `index.html` (single-file app — no build step required)
- `css/lws-type-system.css` (canonical roles)
- `data/ssot-projects.json` (real Surface Surveys + Omani text from your SSOT)
- `js/supabase.js` (pre-wired)
- `vercel.json` (static hosting config)
- `.gitignore` + `package.json` (GitHub friendly)

---

## 6. Future Enhancements You Can Add Later

- Image insertion from Supabase (the bridge + settings panel are already waiting)
- More layout templates
- Direct "Publish to live site" button (once your main site is also on Vercel)

---

**You are fully set up on your exact stack: GitHub + Vercel + Supabase.**

Open `index.html` locally right now to verify everything works, then run the GitHub commands above.

Questions or need a custom domain / password protection later? Just ask.
