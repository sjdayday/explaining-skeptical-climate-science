# Working notes — Case File 01

## Review of the original paper (arXiv:1206.5845, added to project 2026-08-04)

Reading the full preprint confirmed the draft-1 summary and added material
that draft 2 now incorporates:

1. **Two-stage fitting.** Eq. (1) was first fitted to the *entire* 1850–2010
   record; the authors judged the residuals non-random ("model deficient") and
   read the late drift as the anthropogenic signal, motivating the pre-1950
   refit. Draft 1 described only stage two.
2. **Exact coefficients (their Table 1, calibration 1850–1950):**
   A (60-yr amp) = 0.121 ± 0.016 °C; B (20-yr amp) = 0.041 ± 0.016 °C;
   C = 0.16 ± 0.04 °C/century; T1 = 1998.58 ± 1.3; T2 = 1999.65 ± 1.3;
   fit R² = 0.53. Residual ramp: fitted **1950–2010**, slope 0.66 ± 0.08
   °C/century (R² = 0.59), crosses zero in 1942 (draft 1 loosely said
   "from 1942").
3. **Our replication vs. theirs (NOAA GCAG):** amp60 0.100, amp20 0.043,
   linear 0.23 °C/century, R² 0.46, peaks ≈1997.3 / ≈1998.2, ramp 0.81
   crossing ~1947. Phase agreement within ~1 yr of their Table 1 — strong
   cross-dataset replication; amplitude/ramp differences are dataset vintage.
4. **Free-fit admission.** The paper states a free fit of HadCRUT3 gives
   periods "quite close to" 60/20, and their SI-1 free-fit target is ~64.9 yr.
   They imposed 60 on astronomical grounds. Dovetails with Benestad et al.'s
   65.75/21.5 finding. Now used in Objection 2.
5. **SI-1 validation test.** White noise added to the *assumed-true*
   cycles+line curve; refit 1000×; period recovered (64.11 ± 2.63 vs. 64.93).
   Tests recovery-given-truth, not the false-alarm rate under structured
   noise — the exact gap the Benestad synthetic experiment fills. Now a
   dedicated "comeback" answer.
6. **Multi-secular evidence section:** Cariaco Basin G. bulloides best-fit
   61.5 ± 4 yr; PDO tree-ring reconstruction 59.5 ± 4 yr; Camuffo Mediterranean
   500-yr; Klyashtorin fish stocks; Jevrejeva sea level; Ogurtsov 10Be/14C
   60–64 yr; Jupiter/Saturn ~60-yr synodic/tidal beat. Steel-manned in Part 1;
   answered in comeback 3 (quasi-cycles 50–80 yr ≠ fixed clock; Table S2
   incompatibilities; internal variability in GCMs; false dichotomy).
7. **Aerosols:** they argue residuals 1950s–70s rise linearly (no dip), so no
   sulfate-cooling signature needed; 1880–1910/1910–40 "statistically
   equivalent" to 1940–70/1970–2000.
8. **UHI/LULC:** the 0.66 ramp presented as an *upper limit* on anthropogenic
   (possible urban-heat/land-use contamination), citing i.a. McKitrick &
   Michaels 2004/2007 — itself on the Benestad 38-paper list (cross-linked in
   the document).
9. **Solar mechanism chain:** planets → solar activity → TSI (their revision
   of a solar-cycle-length-based proxy; ACRIM composite relied on) → possible
   cosmic-ray/cloud amplification (Kirkby, Svensmark citations). Several links
   are separately faulted in the same replication study; noted in Objection 5.
10. **Forecast specifics:** anthropogenic warming "masked ... until 2040";
    model high in 2100 ≈ **0.6 °C above 2000** (abstract: "may warm less than
    1 °C by 2100"); vs. "3 to 3.4 °C" they attribute to IPCC; sensitivity
    ~1–1.5 °C/doubling, "slight negative feedback"; post-2000 flatness claimed
    as demonstrated skill.
11. **Scorecard update:** decade means 1996–2005 → 2016–2025 = **+0.47 °C**
    observed — ≈¾ of their whole-century ceiling in two decades (El-Niño-proof
    framing); single recent years already exceed the ceiling.

## The adversarial record (added 2026-08-07)

Fetched from the 2013 ESDD open review (doi:10.5194/esdd-4-451-2013; the
paper's first version, "Agnotology: learning from mistakes"; the revision was
not accepted — editor decision C400, M. Huber, 03 Sep 2013; the expanded
paper appeared in TAC 2016). Extracted texts + full comment roster in
`sources/esdd-open-review/`. All quotations verified verbatim against the
Copernicus PDFs (by the claude.ai session that fetched them, re-checked when
merged here). L&S11-specific defenses and where the case file answers them:

1. **Hypothesis, not discovery** (Loehle C253): periods imported from
   Scafetta's solar work; only phase/amplitude fitted, so "2.5 beats"
   allegedly misses. → comeback 4: Exhibit D grants exactly this framing
   (fixed periods, free phase/amplitude) and still finds phantom cycles;
   importing the period relocates the burden to the contested astronomy
   (Objection 5).
2. **"Did not replicate our method"** (C253, re the synthetic test):
   → comeback 4: the slices use the algebraic twin of Eq. (1); no specific
   discrepancy was named; the inflation/instability is estimator-generic.
3. **SI-1 validation exists** (C253): → already answered (comeback 2).
4. **Free fit "visually almost indistinguishable"** (C253): → folded into
   Objection 2 as a concession: the record can't tell 60 from neighbours.
5. **Predicted the post-2000 flat** (C253): → comeback 1 + Part Three.
6. **Multi-century proxies / "evident at naked eyes"** (Scafetta C318):
   → comeback 3 strengthened: Fig. 4's own best-fit periods 61.5±4 vs
   59.5±4, five repeats, ±4-yr slack = broadband variability, not a
   phase-locked clock; Exhibit D answers the appeal to the eye.
7. Benestad C258 states the core point (not the recipe, not 60-vs-70; ~2
   repeats of noisy data carry no physical significance) and closes with
   "It would indeed be very good news is [sic] Loehle and Scafetta (2011)
   were right" — quoted in comeback 4 with bracketed [if].

**Case 02 flag:** Matthews C304 corrects the ESDD draft's
Dirichlet-conditions wording in the *ice-core* case. When writing Case 02,
state the Fourier point for finite discrete records only (as Case 01
Objection 1 already does) and do not import the draft's continuous-function
framing; check whether the Dirichlet claim survived into the 2016 SM. C257
(Solheim/Humlum/Stordahl/Yndestad) is the authors' defense for Case 02 —
mine it then. C312 + supplement (Scafetta's long rebuttal) and the Rypdal
exchange (C328/C331/C338/C347) remain unmined.

## Draft changelog

### Draft 5 (2026-09-21)
- **Interval-provenance pass (Steve's question):** verified against the preprint
  that the 160-year interval is inherited from the archive, not chosen. The 1850
  start is explicitly data availability — stated twice: Introduction, first
  sentence, p. 3 ("the time when global instrumental temperature estimates are
  first available [Brohan et al., 2006]") and Section 3, p. 10 ("Before 1850
  global instrumental temperature records are not available"). The end is dataset
  vintage only: abstract extrapolates "from 1951 to 2009" (p. 2); Figure 1 legend
  names the "April 8, 2010 dataset" (p. 30). Section 2 merely announces the span
  ("over a 160 year interval," p. 6). No main-text argument that 160 years
  suffices for a 60-year cycle; adequacy argued only retroactively in SI-1,
  pp. 37-38 ("works sufficiently well even on a 100 yr calibration period").
  Contrast: the 1950 calibration cutoff IS explicitly justified (p. 6 — Thompson
  et al. 2009; IPCC 2007; Hegerl et al. 2001 "cutoff year"; Hansen et al. 2007
  aerosol offset). Also p. 3: forcing datasets "for the past 160 years" — the
  span treated as a given horizon throughout.
- Edits: Part One provenance sentence ("the full span the thermometers allow");
  Objection 2 insertion ("the archive set the span; the hypothesis simply had to
  live within it"); methods note gains pinpoint cites; status/footer bumped to
  draft 5. Prose-only; figures unchanged.

### Draft 4.2 (2026-08-09) — resonance primer supplement
- New supplements/resonance-primer.html (template src/supplements/, built by
  build.py step 3 with the shared CSS; no data injection). Content reworked
  from the session's two explanations: the resonant-system recipe (restoring
  force + inertia + weak damping = memory); examples grouped mechanical /
  acoustic / electrical / geophysical (swing, wine glass, Mexico City 1985,
  Millennium Bridge 2000, bottle-blowing as the everyday broadband-noise
  analog, radio tuning as frequency-not-source, quartz, MRI, Bay of Fundy,
  seiches, Laplace resonance, Kirkwood gaps); the three response regimes
  (periodic → amplified; broadband/impulse → rings at own period; trend →
  transmitted) with the summary "selective by frequency, never by source";
  and Objection 5's structure as translation + dilemma, incl. what it does
  NOT claim (no assertion the real climate is a 60-yr resonator; no
  identified physical oscillator; heavy damping → quasi-periodicity, the
  bridge to Objection 2) and the Exercise-5 button mapping.
- Linked from: the word "resonance" inside Objection 5's quoted
  "assumed some kind of selective and potent resonance", and a new first
  entry under Going Deeper → Resonance. Footer links add Q factor.

### Draft 4.1 (2026-08-09) — Exercise 5 push button and ramp display fixed
- Steve's report, confirmed: the Push Now button injected a one-substep
  impulse (Δv ≈ 0.003, ring ≈ 0.026) — ~10× too weak to see against any
  running scenario, and its spike landed on a recorded trace sample only
  ~1 time in 5. Now a one-year pulse (PUSH_F 0.018) sized so a single push
  from rest rings at ≈0.17 (≈ the metronome's steady swing); it spans 4
  trace samples (spike always visible, drawn clipped) and is excluded from
  the forcing chart's autoscale so it doesn't flatten the other traces.
- Charts now use fixed per-scenario scales (adaptive only if outgrown;
  ramp's asymmetric). This removes the artifact Steve described: with
  windowed autoscaling, a monotone ramp's newest point is always the window
  max, so the push line rode the top edge and seemed to "flatten" as the
  axis stretched.
- Disclosures added (punch text + footnote): the "greenhouse ramp" is
  radiative forcing, not CO₂ concentration (forcing ∝ log CO₂, hence
  near-linear); it stabilizes after 240 simulated years to keep the display
  bounded; the ramp scenario's fading 60-yr wobble is the onset transient
  decaying at the damping time (~190 yr) while the trend passes through;
  push-size asymmetry stated (metronome ≈ 30× smaller than ramp peak,
  ≈ 80× smaller than the manual push). Legend chip updated (scales are
  per-scenario, no longer "a common magnified scale").
- Verified in-browser: push-from-silence rings at 0.159; spike spans 4
  samples; ramp draws inside a stable frame with wobble visible; metronome
  fills its scale with the clipped spike and a visible perturbation.

### Draft 4 (2026-08-09) — resonance attribution corrected; toolbox demo rendered
- Steve's correction, verified: "resonance/resonant" never appears in L&S11's
  own text — the lone occurrence in the preprint is in a reference title
  (Minobe 1999, line 640 of the extracted text). The SM's wording is
  "L&S11 assumed some kind of selective and potent resonance" (SM p. 9) —
  a translation of the paper's physics, not a quotation. Objection 5 now
  leads with this precision note, presents the translation as the rebuttal's
  (fair) move, and keeps the wine-glass/system point; the at-a-glance table's
  claim cell restated in the paper's own framing (pre-amplified solar effect
  via calibrated feedbacks); Ex 5 dek likewise corrected.
- NEW Exhibit F (fig6_oscillator): the SM's "replication toolbox"
  demonstration, described in its resonance passage but never printed as a
  figure. Re-implements resonance()/FOscillator() (RK4, dt 0.1 yr, T₀ 60 yr,
  ζ 0.05) and decomposeFT (50 harmonics, Gaussian amplitudes ∝ 1/√i), from
  github.com/brasmus/replicationDemos; both R files archived under sources/
  with provenance headers (decomposeFT verified against the repo's FT.R,
  fetched 2026-08-09). Disclosed in caption + methods: the shipped
  resonanceTest() driver halts at a stray stop() (line 120) before its
  sinusoid/noise/CO₂ panels, so the exhibit completes the described
  sequence; row C uses an illustrative ln CO₂ ramp where the driver used
  Mauna Loa. Diagnostics print in the build output (seed 42): response
  dominant period 60.0 yr under structureless noise; 60-vs-11-yr response
  power ratio ≈380× under an 11-yr beat.
- Provenance of this draft: merged from the claude.ai "resonance" session
  (root resonance/ directory, gitignored), whose base was v4.5 — only its
  Objection-5/Exhibit-F changes were grafted onto the current draft; its
  copies of the Obj-2 concession, fourth defense, and adversarial-record
  entries were already present via v5.2 and were not re-applied.
- Status bumped to Draft 4 (header meta, footer, CLAUDE.md).

### Draft 3.2 (2026-08-07) — the ESDD open-review record merged in
- Merged the claude.ai "aftermath-debate" research (based on an older draft)
  into the current template, adapted to the draft-3 register:
  - Comebacks retitled "Four defenses, four answers"; new preamble noting all
    four defenses are on the written record of the 2013 ESDD open review.
  - NEW fourth defense (id `#defense-hypothesis`): Loehle C253's hypothesis
    framing + "did not replicate our method" charge, answered via Exhibit D;
    closes with Benestad C258's "very good news [if]" line.
  - Comeback 3 strengthened with Scafetta C318 ("evident at naked eyes") and
    the Figure-4-proxies-on-their-own-terms answer.
  - Objection 2 gains Loehle's free-fit concession ("visually almost
    indistinguishable", C253).
  - Going deeper gains "The adversarial record" (DOI + discussion page, both
    verified live); Sources footer cites the ESDD exchange.
  - `sources/esdd-open-review/` added (CC-BY extracted texts C253/C258/C318/
    C304 + roster README with PDF URL pattern).
- The "aftermath-debate/" directory at the repo root is the raw material for
  this merge (gitignored; removable once this draft is accepted).

### Draft 3.1 (2026-08-07) — "Working from the source paper to the rebuttal"
- New case-file section (id `#from-the-source`, between IN BRIEF and the
  Glossary) for readers who start from L&S11 itself: nine "stations" in the
  paper's reading order, each quoting verbatim the passage where a challenged
  method choice is made (cited by section and arXiv-preprint page), showing
  the figure that results where there is one, and linking to the objection
  and exercise that address it. Stations: (1) mechanism as speculation, §2
  p. 5 → Obj 5/Ex 5; (2) the 1950 dividing line assumed, §2 p. 6 → Obj 4/
  Ex 4; (3) periods imported + free fit "quite close", §2 pp. 6–7 → Obj 1–2/
  Ex 1–2; (4) failed full fit → refit to 1950, §2 p. 7 (their Figs. 1–2) →
  Obj 1/2/4; (5) residual = human share + "very unlikely ... by chance", §2
  p. 8 (their Fig. 3) → Obj 3/Ex 3; (6) "cannot be simply random noise ...
  factoring it out", §3 p. 12 (their Fig. 4) → Obj 3 + proxy defense; (7)
  the forecast, §6 pp. 15–16 and §8 p. 20 (their Fig. 5) → Part Three/Ex 4;
  (8) ACRIM/solar-cycle-length reliance, §7 p. 17 + SI §b → Obj 5; (9) the
  white-noise validation, SI §a p. 38 (their Fig. Sup. 1, target 64.93 yr) →
  validation defense/Obj 3.
- New `src/extract_ls11_figures.py` (dep: pymupdf) crops the six figures
  unaltered from the preprint PDF at 2× (axis labels and printed legends
  preserved); build.py runs it and injects {{LS11FIG*}} placeholders. Built
  HTML grows to ≈2.4 MB.
- Anchors added: `#exhibit-b`, `#defense-plateau`, `#defense-validation`,
  `#defense-proxies`. Copyright note in-section: quotes/figures © the
  authors, reproduced for commentary and criticism.

### Draft 3 (2026-08-07) — neutral-tone rework of the case-file prose
- Same register as the exercise pass, applied to the main document. Notable
  changes: dek no longer says replication "took the argument apart" (now
  "what replication revealed about the method"); "in one breath" → "in
  brief"; Part 1 "given its best shot" → "at its strongest"; "argument's
  engine" → "key premise"; "That ramp, they said, is us" → "is the human
  contribution"; "File that away" → "Objection 2 returns to this"; "The
  supporting cast" → "The supporting evidence"; Obj 2 closer restated ("A
  constant of nature should not change when the dataset changes…"); Obj 5
  whisper/shout → small/large push (wine-glass analogy kept, restated);
  Part 3 retitled "What happened after publication" (was "The test nature
  ran anyway"; ex5 nav link updated); "budget arithmetic is brutal" → "the
  arithmetic is simple"; "premise smuggles in the conclusion" → "assumes
  the conclusion"; "Five lines that carry the argument" → "The argument in
  five sentences" (label FOR CONVERSATIONS → IN BRIEF); glossary entries
  reworded (no "hugs/knobs/cheap/real currency"; "nature administered" →
  dated plainly).
- Kept: the document title, objection headings, the tightly mapped analogies
  (melody/notation, smoke detector, wine glass, elephant, playground swing),
  "wiggly/wiggle-match" as descriptive terms, and all numbers.
- Status bumped to Draft 3 (header meta and footer).

### Draft 2.3 (2026-08-07) — neutral-tone pass over the exercises
- Reworded the five exercise pages and the case file's trybox/going-deeper
  additions for a straightforward, non-confrontational register: "The game" →
  "The exercise"; removed button emojis; "New random universe" → "New random
  series"; "hug" → "match/fit"; "pure dice" → "randomly generated data";
  dropped flourishes ("Gorgeous", "proud of the hug", "the R² readout
  applauds", "the eye is a poor referee", "what a too-short window sounds
  like", "resonance answers to tempo, not identity" reworded).
- Ex 1: the 60-unit wave's amplitude readout now uses per-graph units
  (±$ for the stock walk, ±m for the ridge, ±% of population, ± arbitrary
  units for random) instead of the truncated y-axis label ("share price");
  label renamed "Its amplitude here"; per-graph captions restated as neutral
  observations (e.g. population: rises and dips have historical causes).
- Ex 4: "Memorizing the past / Missing the future" meters → "Fit to the
  past / Forecast error"; "knob" → "slider" throughout; dropped "The
  scissors" nickname.
- Ex 5: whisper/shout wording replaced with small/large push (the wine-glass
  analogy retained, restated neutrally); fixed the manual-push guidance
  ("about one gridline apart" — gridlines are 60 yr, the earlier text said
  "a couple").
- Kept the analogies that map tightly and already anchor the case file:
  melody/notes (Ex 1), smoke detector (Ex 3), wine glass (Ex 5), Von
  Neumann's elephant (Ex 4).
- Case-file main prose untouched (its register is a separate decision).

### Draft 2.2 (2026-08-06) — “Going deeper” links
- New case-file section (id `#going-deeper`, before the footer): curated
  external explainers for the concepts the document assumes — Fourier
  rebuilds (Jez Swanson interactive; 3Blue1Brown video; Wikipedia), least
  squares (Math is Fun worked example; StatQuest; Wikipedia), R² (StatQuest;
  Wikipedia), the thermometer records (Met Office HadCRUT3; NOAA
  NOAAGlobalTemp; datasets/global-temp mirror), the astronomical provenance
  of the 60/20-yr periods (great conjunction ≈19.86 yr, three beats ≈60;
  Scafetta 2010, arXiv:1005.4639; AMO), overfitting (+ Von Neumann's
  elephant), and resonance (+ harmonic oscillator).
- Primary documents subsection: L&S11 published DOI + arXiv preprint,
  Benestad et al. 2016 open-access DOI (supporting material on the same
  page), and the replicationDemos R package — corrected home:
  github.com/brasmus/replicationDemos.
- Each exercise footnote gains a matching “Learn more” line plus a link back
  to `#going-deeper`.
- All external links verified live 2026-08-06 (WebSearch/WebFetch).

### Draft 2.1 (2026-08-04) — interactive exercises
- Added five interactive exercise pages under `exercises/`, one per objection,
  linked from “try it yourself” boxes in Part Two (anchors `#objection-1`…`-5`
  added; Part Three got `#part-three`):
  1. `ex1-waves.html` — Fourier rebuild of arbitrary graphs (synthetic stock
     walk, fractal skyline, European population 0–2025 CE from McEvedy & Jones
     1978/UN estimates on a log scale, seeded random graphs); wave-budget
     slider; every graph's own “60-unit wave” shown with its amplitude.
     Decomposition runs on a mirrored copy to avoid wrap-around edge
     artifacts.
  2. `ex2-rhythm.html` — live period dial 30–100 yr refitting Eq. (1) on the
     1850–1950 window; beat brackets; visited-period trail; “reveal the full
     scan” with markers at 60 / 65.75 (Benestad) / best-on-this-data.
     In-browser fit reproduces the Python numbers exactly (R² 0.457 at 60,
     0.592 at 87.5).
  3. `ex3-phantom-cycles.html` — the Benestad synthetic experiment live:
     seeded 10,000-yr structured noise (seed shown, re-rollable), 62 slices,
     running histogram vs. true content and the real record's 0.118 °C
     (1850–2010 estimator). Browser RNG ≠ numpy, so values differ from
     Exhibit D per seed; instability is the finding (footnote discloses).
  4. `ex4-hidden-years.html` — overfitting game: line + k harmonics fitted
     1850–2010, curtain over 2011–2025, train-R² vs. future-RMSE meters, the
     “scissors” chart across all 25 knob positions; L&S11-recipe misses
     (≈0.34 °C avg, ≈0.7 °C in 2024) computed live and match Exhibit E.
  5. `ex5-resonance.html` — damped oscillator (60-yr period, Q=10) with four
     pushes: resonant metronome, random weather noise, greenhouse ramp
     (climbs 240 yr then holds so the display stays bounded), manual impulse.
     Noise forcing measures ≈60-yr response rhythm — the Objection 3 tie-in.
- Build: `src/exercises/` templates + `_shared.css`/`_shared.js` (palette,
  seeded PRNG, least squares identical to make_figures.py, canvas charts);
  `build.py` step 3 injects shared assets + GCAG JSON.
- All pages carry “honest labels” footnotes (real vs. synthetic vs. schematic,
  seeds, method equivalences), per the working conventions.
- Ex 1 addendum: a second chart, x-aligned under the target, shows the waves
  themselves at true size — waves already in the rebuild in light gray, waves
  just added by the slider in light blue, the near-60-unit wave always in
  amber (with its strength rank reported); the magnified 60-unit panel below
  is unchanged.

### Draft 2 (2026-08-04)
- Checked against the original preprint (now in project files).
- Part 1: two-stage fit; model equation displayed; free-fit ≈65 note;
  supporting-cast subsection; expanded conclusions (50±10% natural of 0.8 °C;
  60% of 1970–2000 warming from cycles; aerosol argument; UHI upper-limit +
  M&M cross-link; sensitivity 1–1.5 °C; 0.6 °C-by-2100 forecast; plateau
  claimed as skill).
- Exhibit B caption: coefficient-by-coefficient comparison with Table 1;
  residual-panel legend corrected (fit window 1951–2010, zero-crossing ~1947).
- Objection 2: their own free fit vs. imposed 60.
- Objection 5: contested mechanism-chain links.
- Comebacks: expanded to three (plateau; SI-1 white-noise validation;
  multi-secular proxies).
- Part 3: century-budget arithmetic (decadal means).
- Table, talking points, methods, sources updated accordingly.

### Draft 1 (2026-07-31)
- Initial case file: steel-man, five objections, aftermath, table, talking
  points, glossary; five figures; replication on NOAA GCAG; synthetic-noise
  experiment.

## Open items / ideas for future drafts
- Optional Exhibit: side-by-side of L&S11 SI-1 (white noise, cycle assumed)
  vs. Benestad-style structured noise (no cycle) as a single teaching graphic.
- Consider a short "how to present this in 5 minutes" speaker sheet.
- Sensitivity of the period scan (Exhibit C) to calibration window choice.
- If HadCRUT5 becomes easily fetchable in-environment, add a second-dataset
  panel to Exhibit B.
