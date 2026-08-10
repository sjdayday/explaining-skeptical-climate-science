# CLAUDE.md — climate-explain / humlum-greenland-ice-core

## What this directory is

Case File 02 in the series explaining climate-skeptic papers **and** their
rebuttals to general audiences. This one covers Humlum, Solheim & Stordahl
(2011) ("HSS11a": three long Fourier cycles fitted to the most recent 4,000
years of the GISP2 Greenland ice-core record) and the "Selective use of
data" section of the Benestad et al. (2016) supporting material (SM pp. 5–8,
Figure S1, R function `Humlum.et.al.2011()`). The deliverable is a single
self-contained HTML explainer plus fully reproducible figures, following the
model established by Case File 01 (`../loehle-scafetta-curve-fitting/`).

Read `NOTES.md` before making analytical changes — it holds the source
inventory, the full review of the primary paper, verified facts, the draft
changelog, and open items.

## Working conventions (same as Case 01 — do not drift)

- **Steel-man first.** Part One presents HSS11a at its strongest before any
  rebuttal — including their genuine Svalbard 1991–2010 truncation test and
  the caveats the paper itself states. Every quotation must be verified
  against the primary PDF in `sources/`.
- **Precision norms.** The window is the most recent 4,000 years *of a
  ~50,000-year file*: by sample count that is 395 of 1,631 (24%), by time
  span 8%. Say which. Ages are years before 1950; the youngest sample is
  ≈1855 CE — distinguish "present" (1950) from the record's end (~1855)
  and from today. The fair out-of-window test is the rest of the *Holocene*
  (4–11.7 kyr BP), not the glacial period — quote glacial mismatches only
  as context.
- **Honest labeling.** All figures use the real GISP2 series (NOAA file in
  `data/`). Our fitted curves replicate the SM's demonstration (periods
  fixed at 2,804/1,186/556 yr, least squares on the ≤4 kyr window); HSS11a's
  own analysis was wavelet-based — never present our coefficients as theirs.
  Both extension variants (trend kept / trend zeroed) are shown.
- **Structure encodes the debate.** Amber = claim, teal = rebuttal, ink =
  observations, grey = the discarded data. Same dual-rail design system and
  CSS as Case 01. Exhibits lettered A–…
- **Reproducibility is part of the argument.** Every number regenerates from
  `src/build.py` (deterministic; no RNG in this case). If you change an
  analysis, rerun the build and update captions/notes in the same commit.

## Build

```bash
cd src && python3 build.py     # deps: numpy, matplotlib
```

(Use the repo venv: `/Users/steve/git/climate-explain/.venv/bin/python3 build.py`.)

Output: `../figures/*.png` and `../casefile02-humlum-greenland-ice-core.html`
(figures embedded as base64). Edit prose in `src/casefile02_template.html`,
never in the built HTML.

## Data

`data/gisp2_temp_accum_alley2000.txt` = GISP2 temperature + accumulation
(Alley 2000/2004), fetched 2026-08-09 from NOAA NCEI (refresh command in
`README.md`; the file is archival and should not change). Temperature
section: file lines 76–1711; 1,631 samples, 0.0951–49.981 kyr BP,
−53.6…−28.7 °C. Ages are kyr before 1950.

## Sources

- `sources/Identifying_natural_contributions_to_late_Holocene.pdf` — true
  PDF, **the primary paper** (HSS11a: Global and Planetary Change
  79:145–156, doi:10.1016/j.gloplacha.2011.09.005; supplied 2026-08-10).
  Cite by journal pages: PDF page N = printed page 144+N. NOTES.md holds
  the full review (quotes, numbers, r² reconciliation).
- `sources/Advances in Meteorology - 2012 - Solheim - Solar Activity and
  Svalbard Temperatures.pdf` — true PDF, the companion paper (Solheim,
  Stordahl & Humlum, Adv. Met. 2011, doi:10.1155/2011/543146). Its ref. [3]
  is HSS11a; it predicts a Svalbard annual-mean **decrease of 3.5 ± 2 °C**
  for solar cycle 24 (2009–20), winter ≈6 °C — the falsifiable forecast.
- Shared Benestad materials moved to the repo root: `../sources/
  benestadetalnccSM2014.pdf` (**zip archive despite the name**; per-page
  `{n}.txt` + `{n}.jpeg`). The HSS11a case is SM pp. 5–8 + Figure S1
  (p. 57) + Table S1 entry (p. 62). The ESDD open-review record for the
  rebuttal's first version is in
  `../loehle-scafetta-curve-fitting/sources/esdd-open-review/` (C257 —
  Solheim, Humlum, Stordahl & Yndestad's defense — is in the roster but not
  yet extracted; C304 (Matthews) corrected the draft's Dirichlet-conditions
  claim, which the final SM dropped — verified 2026-08-09).

## Current state (draft 2, 2026-08-10)

Replication numbers on the NOAA file (SM-style fit, periods 2804/1186/556
yr + linear trend, least squares on ages ≤ 4 kyr BP): in-window R² 0.852,
RMSE 0.30 °C, trend +0.445 °C/kyr (toward the past — the late-Holocene
cooling), amplitudes 0.32/0.47/0.27 °C. Extended over the rest of the
Holocene (4–11.7 kyr BP): mean error −3.22 °C, RMSE 4.45 °C, R² −2.9
(trend kept); RMSE 2.39 °C (trend zeroed); within the paper's own claimed
10–25%-of-record forecasting range (4–5 kyr BP) RMSE 1.66 °C / 1.02 °C.
Their own reported numbers: GISP2 r² 0.63 (periods 2804/1186/556 by
nonlinear optimization; Fourier peaks 3598/1139/788/584/366); Svalbard r²
0.47 full / 0.36 truncated. Youngest sample 1855 CE; used window = 8% of
the record's span. Draft 2 steel-man is sourced from the primary PDF.
Still absent: exercises; "from the source" section (needs figure crops);
C257 defenses; Svalbard observed-data verification exhibit.

## Sibling cases

`../loehle-scafetta-curve-fitting/` — Case 01, the established model
(exercises, supplements, from-the-source section). Next: Douglass et al.
(2007) statistical-interval mix-up as Case 03.
