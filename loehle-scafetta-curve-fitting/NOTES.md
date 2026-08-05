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

## Draft changelog

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
