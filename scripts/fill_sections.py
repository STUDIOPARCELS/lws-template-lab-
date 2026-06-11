#!/usr/bin/env python3
"""
FILL stage (Build Plan A1/A2).

Takes the 13 template-lab section definitions — transcribed EXACTLY from
index.html `loadTemplate()` (same layers, same x/y/w/h, same .lws-* roles) —
and fills them with every project's real SSOT content. Renders per-project
SECTION REVIEW SHEETS using the lab's own export pipeline
(`buildComposedPageHTML`: 1280x720 canvas, equal top/bottom padding fit).

Rule #1: never freestyle. The .lws-* type CSS is extracted VERBATIM from
index.html at build time, so the sheets can never drift from the lab.

Outputs:
  data/filled-sections.json   project -> filled sections (the FILL artifact)
  review/<project>.html       review sheet per project
  review/index.html           directory
"""
import json, re, html as H
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SSOT = json.loads((ROOT / "data/ssot-projects.json").read_text())["projects"]
MANIFEST = json.loads((ROOT / "data/image-manifest.json").read_text())
PUBLIC = MANIFEST["publicBase"].rstrip("/") + "/"

# ---------------------------------------------------------------- lab CSS (verbatim)
src = (ROOT / "index.html").read_text()
css_lines = [l for l in src.splitlines()
             if re.match(r"\s*(@import url\('https://fonts|:root\{--lws|\.lws-)", l)]
LAB_CSS = "\n".join(dict.fromkeys(css_lines))  # dedupe, keep order

def clip(s, n):
    """Word-boundary truncation — same behavior as the lab's clip()."""
    s = (s or "").strip()
    if len(s) <= n: return s
    cut = s[:n]; sp = cut.rfind(" ")
    if sp > n * 0.5: cut = cut[:sp]
    return re.sub(r"[\s,;:.—–-]+$", "", cut) + "…"

def T(role, content, x, y, w, h):  return {"type":"text","role":role,"content":content,"x":x,"y":y,"w":w,"h":h}
def IMG(label, x, y, w, h):        return {"type":"image","content":label,"x":x,"y":y,"w":w,"h":h}

# ------------------------------------------------- the 13 templates (from loadTemplate)
def build_sections(p):
    narr = p.get("narrative",""); year = p.get("year",""); loc = p.get("location","")
    ds = p.get("descriptionSections",{}) or {}; aa = p.get("artworkAtoms",{}) or {}
    title = p.get("title","");
    sci = ds.get("scientific","")   # exact lab binding (no fallback)
    vis = ds.get("visual","")       # exact lab binding (no fallback)
    atm = ds.get("atmospheric","")
    mat = aa.get("material",""); printer = aa.get("printer","")
    S = {}
    S["full-image-hero"] = [IMG("IMAGE PLACEHOLDER",0,35,100,30),
        T("metadata-value", f"{year}  •  {loc}",68,68,28,5),
        T("description-section-value", clip(narr,210),68,74,28,14)]
    S["split-hero"] = [IMG("IMAGE PLACEHOLDER",0,0,52,100),
        T("project-title-h1",title,56,12,40,10), T("narrative-description-body",clip(narr,420),56,24,40,28),
        T("metadata-key","YEAR",56,58,10,4), T("metadata-value",year,66,58,20,4)]
    S["editorial"] = [T("project-title-h1",title,8,6,84,8),
        T("narrative-description-body",clip(narr,380),8,16,84,22),
        T("description-section-label","VISUAL",8,42,20,4), T("description-section-value",clip(vis,220),8,46,84,12),
        IMG("IMAGE PLACEHOLDER",8,62,84,28)]
    S["metadata-desc"] = [T("metadata-key","YEAR",8,12,10,4), T("metadata-value",year,18,12,30,4),
        T("metadata-key","LOCATION",8,20,14,4), T("metadata-value",loc,22,20,50,4),
        T("description-section-label","ATMOSPHERIC",8,32,24,4), T("description-section-value",atm,8,36,84,12)]
    S["full-bleed"] = [IMG("IMAGE PLACEHOLDER",0,0,100,72),
        T("project-title-h1",title,8,76,84,7), T("metadata-value",f"{year}  •  {loc}",8,88,84,5)]
    S["text-first"] = [T("project-title-h1",title,8,10,84,7), T("narrative-description-body",narr,8,20,74,30),
        T("description-section-label","SCIENTIFIC / FACTUAL",8,56,44,4), T("description-section-value",sci,8,61,84,18)]
    tw,ty,th,gap,x0 = 23.5,23,68,1.6,13.2
    parent = p.get("parent") or "Photography"
    pname = re.sub(r"^Surface Surveys:\s*","",title,flags=re.I)
    caps = ["/ "+parent, "/ "+pname, "/ "+str(year)]
    tri=[T("project-title-h1",title,8,6,84,7)]
    for i in range(3):
        ix = x0 + i*(tw+gap)
        tri += [T("caption",caps[i],ix,18,tw,3), IMG(f"IMAGE {i+1}",ix,ty,tw,th)]
    S["triptych"]=tri
    S["specifications"] = [T("project-title-h1",title,8,8,84,7),
        T("metadata-key","YEAR",8,22,14,4), T("metadata-value",year,24,22,30,4),
        T("metadata-key","LOCATION",8,30,16,4), T("metadata-value",loc,24,30,62,4),
        T("artwork-atom-label","MATERIAL",8,44,24,3), T("artwork-atom-detail",mat,8,48,84,6),
        T("artwork-atom-label","PRINTER",8,58,24,3), T("artwork-atom-detail",printer,8,62,84,5)]
    S["duo"] = [IMG("IMAGE 1",0,0,50,58), IMG("IMAGE 2",50,0,50,58),
        T("project-title-h1",title,8,63,84,7), T("narrative-description-body",clip(narr,300),8,72,84,18)]
    gw,gh,gx,gy,ggx,ggy = 12,32.4,23,16,2,3.2
    S["grid-8"]=[IMG(f"IMAGE {r*4+c+1}", gx+c*(gw+ggx), gy+r*(gh+ggy), gw, gh) for r in range(2) for c in range(4)]
    qw,qx,qgx = 19.125,8,2.5
    S["grid-4"]=[IMG(f"IMAGE {c+1}", qx+c*(qw+qgx),22,qw,56) for c in range(4)]
    S["quote"] = [IMG("IMAGE",8,22,30,50),
        T("pull-quote","“The final film and image series didn’t just elevate our campaign — it redefined how our audience perceives us.”",42,24,50,34),
        T("description-section-label","NAME — ROLE  /  COMPANY",42,62,50,5)]
    S["annotated"] = [IMG("IMAGE",8,8,84,84),
        T("description-section-label","DESIGN & STRATEGY",8,3.5,40,4),
        T("description-section-label",title,54,3.5,38,4),
        T("description-section-label","LISA WOOD STUDIO",8,92.5,40,4),
        T("description-section-label",loc or "",54,92.5,38,4)]
    return S

# ------------------------------------------------- image wiring (manifest folders)
def url(path): return PUBLIC + quote(path, safe="/")
KNOWN = {
 "flipped": [url(f"flipped/final-photos/web-2000px/{n}") for n in
   ["flipped-02-1.webp","flipped-01-1-zoom.webp","flipped-04-2.webp","flipped-07-3.webp",
    "flipped-09-4.webp","flipped-11-5.webp","flipped-13-6.webp","flipped-05-3-zoom.webp",
    "flipped-08-4-zoom.webp","flipped-10-5-zoom.webp","flipped-12-6-zoom.webp","flipped-16-gemini-generated-image-nbtz0rnbtz0rnbtz-1.webp"]],
 "side-effects": [url(f"SIDE EFFECTS/{n}") for n in
   ["1.jpg","2.jpg","3.jpg","4.jpg","SIDE EFFECTS 1 2 BLENDER FINAL ARTWORK.png","SIDE EFFECTS 3 4 FINAL ALL LAYERS copy - Copy.png"]],
}
def wire_images(pid, sections):
    pool = KNOWN.get(pid);
    if not pool: return sections
    i = 0
    for name, layers in sections.items():
        for l in layers:
            if l["type"]=="image":
                l["imageUrl"] = pool[i % len(pool)]; i += 1
    return sections

# ------------------------------------------------- lab export math (buildComposedPageHTML)
def render_section(layers):
    # FIXED 1280x720 canvas — exactly as tuned in the lab. Exact x/y/w/h percentages,
    # no fit/rescale. This is the canvas the user designs on (16:9, centered on page).
    out=['<section style="width:100%;max-width:1280px;aspect-ratio:16 / 9;margin:0 auto;position:relative;background:#faf8f5;overflow:hidden;">']
    for l in layers:
        st=f'position:absolute;left:{l["x"]}%;top:{l["y"]}%;width:{l["w"]}%;height:{l["h"]}%;'
        if l["type"]=="text":
            out.append(f'<div style="{st}" class="lws-{l["role"]}">{H.escape(l["content"]).replace(chr(10),"<br>")}</div>')
        elif l.get("imageUrl"):
            out.append(f'<img src="{l["imageUrl"]}" alt="" style="{st}object-fit:cover;object-position:50% 50%;border:none;">')
        else:
            out.append(f'<div style="{st}border:2px dashed #e67e22;background:#fffbeb;display:flex;align-items:center;justify-content:center;color:#c85a17;font-size:11px;">{H.escape(l["content"])}</div>')
    out.append("</section>")
    return "".join(out)

CHROME = """<style>body{margin:0;background:#efece7;font-family:system-ui;}
.bar{max-width:1280px;margin:36px auto 10px;display:flex;justify-content:space-between;align-items:baseline;
 font-family:'Space Mono',monospace;font-size:11px;letter-spacing:.14em;color:#8a8f96;text-transform:uppercase;
 border-bottom:1px solid #d8d4cd;padding-bottom:6px;}
.bar b{color:#2b2b2b;} .head{max-width:1280px;margin:40px auto 6px;padding:0 2px;}
.head h1{font-family:'Space Mono',monospace;font-size:15px;letter-spacing:.22em;color:#2b2b2b;margin:0;}
.head p{font-family:'Space Mono',monospace;font-size:11px;letter-spacing:.1em;color:#8a8f96;margin:6px 0 0;}
.shadow{box-shadow:0 1px 14px rgba(0,0,0,.07);margin-bottom:6px;}</style>"""

ORDER = ["full-bleed","full-image-hero","split-hero","editorial","text-first","triptych",
         "duo","grid-8","grid-4","metadata-desc","specifications","quote","annotated"]
LABEL = {"full-bleed":"HERO — FULL BLEED","full-image-hero":"HERO — FULL IMAGE","split-hero":"HERO — SPLIT",
 "editorial":"NARRATIVE — EDITORIAL","text-first":"NARRATIVE — TEXT FIRST","triptych":"IMAGE STUDY — TRIPTYCH",
 "duo":"IMAGE STUDY — DUO","grid-8":"IMAGE STUDY — GRID 8","grid-4":"IMAGE STUDY — GRID 4",
 "metadata-desc":"SPECS — METADATA","specifications":"SPECS — SPECIFICATIONS","quote":"QUOTE / TESTIMONIAL","annotated":"PLATE — ANNOTATED"}

review = ROOT/"review"; review.mkdir(exist_ok=True)
filled = {}
for p in SSOT:
    pid = p["id"]
    secs = wire_images(pid, build_sections(p))
    filled[pid] = {"title":p["title"],"parent":p.get("parent",""),"sections":secs}
    body = [f'<div class="head"><h1>{H.escape(p["title"].upper())}</h1>'
            f'<p>SECTION REVIEW SHEET — all 13 template sections filled with this project’s SSOT text · confirm / comment / kill each · {H.escape(p.get("parent",""))}</p></div>']
    for i,name in enumerate(ORDER,1):
        body.append(f'<div class="bar"><span><b>{i:02d}</b> · {LABEL[name]}</span><span>{name}</span></div>')
        body.append(f'<div class="shadow">{render_section(secs[name])}</div>')
    page = (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{H.escape(p["title"])} — Section Review</title><style>{LAB_CSS}</style>{CHROME}</head><body>'
            + "".join(body) + '<div style="height:80px"></div></body></html>')
    (review/f"{pid}.html").write_text(page)

# directory
groups = {}
for p in SSOT: groups.setdefault(p.get("parent","Other"), []).append(p)
items = []
for g in ["Photography","Installation","Surface Surveys","Luxuriate in Discomfort"]:
    if g not in groups: continue
    items.append(f'<h2>{g}</h2>')
    for p in groups[g]:
        items.append(f'<a href="{p["id"]}.html">{H.escape(p["title"])}</a>')
(review/"index.html").write_text(
 '<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
 '<title>Section Review Sheets</title><style>'
 "body{font-family:'Space Mono',monospace;background:#efece7;color:#2b2b2b;max-width:680px;margin:60px auto;padding:0 20px;}"
 'h1{font-size:16px;letter-spacing:.22em;}h2{font-size:11px;letter-spacing:.18em;color:#8a8f96;margin:34px 0 8px;text-transform:uppercase;}'
 'a{display:block;color:#2b2b2b;text-decoration:none;font-size:14px;padding:9px 0;border-bottom:1px solid #d8d4cd;}a:hover{color:#e67e22;}'
 f'</style><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Mono&display=swap"></head><body>'
 '<h1>SECTION REVIEW SHEETS</h1><p style="font-size:11px;color:#8a8f96;">FILL stage — your 13 templates × each project’s real text. Confirm, comment, or kill per section.</p>'
 + "".join(items) + "</body></html>")

(ROOT/"data/filled-sections.json").write_text(json.dumps(filled, indent=1, ensure_ascii=False))
print(f"filled-sections.json: {len(filled)} projects · review sheets: {len(list(review.glob('*.html')))} files")
