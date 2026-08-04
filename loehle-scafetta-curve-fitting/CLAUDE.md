# CLAUDE.md — climate-explain / loehle-scafetta-curve-fitting

## What this repo is

Case File 01 in a series explaining climate-skeptic papers **and** their
rebuttals to general audiences. This one covers Loehle & Scafetta (2011)
("empirical decomposition", 60/20-year cycles) and the "Curve-fitting"
section of the Benestad et al. (2016) supporting material. The deliverable
is a single self-contained HTML explainer plus fully reproducible figures.

Read `NOTES.md` before making analytical changes — it holds the paper
review, the accuracy audit, the draft changelog, and open items.

## Working conventions (do not drift from these)

- **Steel-man first.** Part One presents the original paper at its
  strongest, with its own numbers, before any rebuttal. Fairness is a
  feature the audience will test.
- **Precision norms.** Distinguish rates from counts; fit windows from
  zero-crossings (their ramp: fitted 1950–2010, crosses zero 1942); state
  dataset vintage whenever quoting replication numbers. Steve will catch
  imprecise language.
- **Honest labeling.** Real data (NOAA GCAG) vs. schematic (Exhibit A) vs.
  synthetic (Exhibit D) is always stated in the caption. Numerical
  differences from the original paper are disclosed, not smoothed over.
  Construction-dependent results (e.g. the ~14× vs ~4× inflation factor)
  are framed as instability findings, never as point estimates.
- **Structure encodes the debate.** Amber = claim, teal = rebuttal,
  ink = observations, throughout prose, figures, and CSS. Exhibits are
  lettered A–E. Keep the dual-rail design system.
- **Reproducibility is part of the argument.** Every number in the document
  must regenerate from `src/build.py`. If you change an analysis, rerun the
  build and update the affected captions/notes in the same commit.

## Build

```bash
cd src && python3 build.py     # deps: numpy, pandas, matplotlib
```

(On this machine the system python3 lacks the deps; use the gitignored repo
venv: `/Users/steve/git/climate-explain/.venv/bin/python3 build.py`.)

Deterministic (seed 42). Output: `../figures/*.png`,
`../casefile01-loehle-scafetta-curve-fitting.html` (figures embedded as
base64), and `../exercises/*.html` — five interactive exercise pages, one per
objection, built from `src/exercises/exN_*_template.html` plus
`src/exercises/_shared.{css,js}` with the GCAG data injected as JSON. Edit
prose in `src/casefile01_template.html` and the exercise templates, never in
the built HTML. The exercises follow the same conventions: honest-labels
footnote on every page, seeded randomness, the amber/teal/ink palette, and
in-browser fits that reproduce the Python numbers (Ex 3's browser RNG differs
from numpy by design; its footnote says so).

## Data

`data/annual.csv` = NOAA NOAAGlobalTemp (source `GCAG`, anomalies vs.
20th-century mean, 1850–2025) + GISTEMP, via the `datasets/global-temp`
GitHub mirror. Refresh command is in `README.md`. Refreshing shifts the
replication numbers slightly; if you refresh, update the methods note and
Exhibit captions together.

## Sources (`sources/`)

- `loehlescafetta1206_5845v1.pdf` — true PDF, the L&S11 arXiv preprint.
- `Learningfrommistakesinclimateresearchs0070401515975.pdf` and
  `benestadetalnccSM2014.pdf` — **zip archives despite the .pdf names**
  (per-page `{n}.txt` + `{n}.jpeg`). Unzip to read; concatenate the .txt
  files in numeric order for full text. Table S3 of the SM (pages 64–67)
  is image-only.

## Current state (draft 2, 2026-08-04)

Key replication numbers on this data snapshot: calibration 1850–1950 gives
60-yr amplitude 0.100 °C, 20-yr 0.043 °C, R² 0.457, cycle peaks ≈1997/1998
(their Table 1: 0.121±0.016, 0.041±0.016, R² 0.53, peaks 1998.6/1999.7);
residual ramp 0.81 °C/century crossing ~1947 (theirs: 0.66±0.08 crossing
1942); period scan best ≈87.5 yr vs R² 0.457 at 60; synthetic slices:
amplitudes 0.007–0.139 °C, mean ≈13.7× the series' true 60-yr content;
observed decadal warming 1996–2005 → 2016–2025 = +0.47 °C vs. their
≈0.6 °C-above-2000 ceiling for 2100.

## Next in the series

Sibling directories under `climate-explain/`: Humlum et al. (2011)
discarded ice-core data; Douglass et al. (2007) statistical-interval
mix-up. Follow the same case-file structure and conventions.
