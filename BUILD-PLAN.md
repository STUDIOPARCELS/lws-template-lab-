# Build Plan — the repeatable, self-improving loop to auto-composed pages

**Goal:** Add a project to the SSOT → the engine composes a publish-ready page
(sections chosen + **ordered by design logic**, content bound, images pulled from
Supabase) → draft on the sandbox preview → Lisa approves → production.

---

## The loop (run for every project — it gets smarter each pass)

```
SELECT project ─▶ RESOLVE images (manifest) ─▶ COMPOSE (sections + order + bind)
      ▲                                                      │
      │                                                      ▼
   LEARN  ◀──────  REVIEW (Lisa, on sandbox)  ◀──────  RENDER (preview)
```

**Why it's recursive:** every REVIEW appends a rule to the **Learnings Log** below.
The composer reads those rules, so **project N+1 starts better than project N**.
Hand-built reference pages teach the rules; once the rules are good, the engine
produces them automatically. That is the engine.

---

## To-do (we tick + refine as we go)

### Stage 0 — Reference: establish the look by hand
- [x] **R1** Photography reference page — **Flipped** (hero → narrative → image study → specs → plate). Live Supabase images. → `demo-flipped.html`
- [ ] **R2** Lock the **Photography page pattern** from Lisa's R1 feedback
- [ ] **R3** Installation reference page (ECS or Mind the Gap) — adds the **Media / video** section
- [ ] **R4** Lock the **Installation page pattern**

### Stage 1 — Codify: turn the look into data
- [ ] **C1** `recipe.json` — per discipline: section set, default order, variation rules
- [ ] **C2** Finalize `image-manifest.json` with real **nested** paths (`web-2000px`), hero + order per project

### Stage 2 — Engine: generate the look automatically
- [ ] **E1** Composer reads SSOT + manifest + recipe → renders a page (no hand-HTML)
- [ ] **E2** Proof: engine-generated Flipped matches hand-built R1
- [ ] **E3** Order logic varies section order per project (the differentiator)

### Stage 3 — Run + recurse: the payoff
- [ ] **G1** Generate all Photography pages → review → log learnings → regenerate
- [ ] **G2** Generate all Installation pages → review → log learnings → regenerate
- [ ] **G3** Bespoke collections: Surface Surveys, Luxuriate in Discomfort

### Stage 4 — Lock + hand off
- [ ] **L1** Package as the "add a project → page appears" agent skill
- [ ] **L2** Promote approved pages sandbox → production

---

## Learnings Log (the memory that makes it recursive)
Every review appends rules here; the composer obeys them.

| # | From | Rule the engine must follow |
|---|------|-----------------------------|
| _(awaiting Lisa's R1 feedback on demo-flipped.html)_ | | |
