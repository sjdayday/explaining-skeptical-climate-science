# Case File 02 — The 4,000-Year Window

General-audience explainer materials for **Humlum, Solheim & Stordahl (2011)**
("HSS11a"), "Identifying natural contributions to late Holocene climate
change" (*Global and Planetary Change* 79:145–156), and its rebuttal in the
supporting material of **Benestad et al. (2016)**, "Learning from mistakes in
climate research" (*Theor. Appl. Climatol.* 126:699–703), section "Selective
use of data."

Part of a series explaining climate-skeptic papers and their rebuttals to
non-specialist audiences: the claim steel-manned first, then the rebuttal,
then the post-publication scorecard. Case File 01 (Loehle & Scafetta 2011)
established the model; this case introduces a new error type — selective use
of data — while reinforcing Case 01's central lesson that a fit is only
tested by data it never touched.

## The case in one paragraph

HSS11a fitted three long cycles (periods ≈2,804, 1,186, and 556 years) to
the most recent 4,000 years of the GISP2 Greenland ice-core temperature
record and proposed that such natural cycles — attributed to solar and
lunar influences — dominate climate change, with testable forecasts of
coming natural cooling. The same public data file continues for another
~46,000 years — 92% of the record's span — which the paper set aside. The
rebuttal extends the fitted curve into that discarded era, where it fails
immediately; the fit that explains 85% of the variance inside its window is
many times worse than useless outside it.

## Contents

| Path | What it is |
|---|---|
| `casefile02-humlum-greenland-ice-core.html` | The explainer — a single self-contained file (figures embedded); open in any browser. |
| `CLAUDE.md` | Standing instructions and current state for Claude Code sessions in this case directory. |
| `NOTES.md` | Working notes: source inventory, verified facts, draft changelog, open items. |
| `sources/` | Primary documents for this case (see `sources/README.md`); shared Benestad materials live in the repo root's `../sources/`. |
| `src/make_figures.py` | Generates the figures: replicates the HSS11a-style fit on the real GISP2 data and the rebuttal's extension into the discarded era. |
| `src/casefile02_template.html` | Document source with `{{FIGn}}` placeholders. |
| `src/build.py` | Regenerates figures and assembles the final HTML. |
| `data/gisp2_temp_accum_alley2000.txt` | The GISP2 temperature reconstruction (Alley 2000/2004), as served by NOAA — the exact file the SM's footnote cites. |

## Rebuilding

```bash
cd src && python3 build.py     # deps: numpy, matplotlib
```

(On this machine use the gitignored repo venv:
`/Users/steve/git/climate-explain/.venv/bin/python3 build.py`.)

Deterministic — no random numbers are used in this case's figures.

## Data provenance

`data/gisp2_temp_accum_alley2000.txt` is the GISP2 temperature and
accumulation dataset, downloaded 2026-08-09 from NOAA NCEI Paleoclimatology:

```bash
curl -sL https://www.ncei.noaa.gov/pub/data/paleo/icecore/greenland/summit/gisp2/isotopes/gisp2_temp_accum_alley2000.txt \
     -o data/gisp2_temp_accum_alley2000.txt
```

Citation: Alley, R.B. 2000, "The Younger Dryas cold interval as viewed from
central Greenland," *Quaternary Science Reviews* 19:213–226; data as Alley
2004, IGBP PAGES/WDCA Contribution Series #2004-013. This is the same file
(same FTP path, modulo https) cited by the Benestad et al. supporting
material, and — per the SM — the same public record underlying HSS11a's
analysis.

Facts verified directly from this file (see `NOTES.md`): 1,631 temperature
samples spanning 0.095–49.98 kyr BP; ages are years before 1950 ("present"),
so the youngest sample is ≈1855 CE; the ≤4 kyr BP window used by HSS11a
holds 395 samples covering 8% of the record's span.

## Honest-labeling commitments

- All figures use the **real** GISP2 series; the fitted curves are our
  replication of the HSS11a-style model (periods fixed at 2,804/1,186/556
  years, amplitudes and phases fitted by least squares to the ≤4 kyr window),
  following the supporting material's `Humlum.et.al.2011()` demonstration.
  HSS11a's own analysis was wavelet-based; period values are theirs, as
  reported in the SM. Numerical differences from their paper are disclosed
  once the primary PDF is in `sources/`.
- The extension into the discarded era is shown in both SM variants (trend
  kept, trend zeroed), since the choice affects how badly the model fails —
  the instability is part of the finding.
- GISP2 is one location in central Greenland, and its record ends ≈1855 CE.
  Every figure caption that touches "the present" states this.

## Primary sources

- Humlum, Solheim & Stordahl (2011), doi:10.1016/j.gloplacha.2011.09.005
  — **PDF not yet in sources/**; the steel-man currently draws on the
  supporting material's quotations and the companion Svalbard paper.
- Solheim, Stordahl & Humlum (2011/2012), "Solar Activity and Svalbard
  Temperatures," *Advances in Meteorology*, doi:10.1155/2011/543146 —
  in `sources/` (the same author cluster; its ref. [3] is HSS11a; source of
  the falsifiable Svalbard forecast).
- Benestad et al. (2016), doi:10.1007/s00704-015-1597-5 + supporting
  material, "Selective use of data" section (SM pp. 5–8) — in the repo
  root's `../sources/`.
