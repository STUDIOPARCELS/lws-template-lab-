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

## 2. Recommended: GitHub + Vercel (Your Usual Stack)

### Step-by-step (PowerShell / Terminal)

```powershell
# 1. Go into the folder
cd "D:\LWS\OBSERVATORY FINAL\WEBSITE\WEBSITE FOLDERS\template-lab"

# 2. Initialize git (only needed once)
git init
git add .
git commit -m "Initial LWS Template Lab — SSOT visual composer with full-image-hero 16:6, undo, Page Builder, Supabase bridge"

# 3. Create a new repo on GitHub.com first (https://github.com/new)
#    Name it something like: lws-template-lab

# 4. Connect and push (replace YOUR_GITHUB_USERNAME)
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/lws-template-lab.git
git branch -M main
git push -u origin main
```

### Connect to Vercel (one time)

1. Go to Vercel dashboard → **Add New Project**
2. Import the GitHub repo you just created (`lws-template-lab`)
3. Vercel auto-detects the static site (thanks to `vercel.json`)
4. Click Deploy
5. Future pushes to `main` will auto-deploy.

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
