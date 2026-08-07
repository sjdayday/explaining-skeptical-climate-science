# Case File 01 — The 60-Year Cycle That Wasn't

General-audience explainer materials for **Loehle & Scafetta (2011)**, "Climate
Change Attribution Using Empirical Decomposition of Climatic Data" (*The Open
Atmospheric Science Journal* 5:74–86), and its rebuttal in the supporting
material of **Benestad et al. (2016)**, "Learning from mistakes in climate
research" (*Theor. Appl. Climatol.* 126:699–703), section "Curve-fitting."

Part of a series explaining climate-skeptic papers and their rebuttals to
non-specialist audiences: the claim steel-manned first, then the rebuttal,
then the post-publication scorecard.

## Contents

| Path | What it is |
|---|---|
| `casefile01-loehle-scafetta-curve-fitting.html` | The explainer — a single self-contained file (figures embedded); open in any browser, print-friendly. |
| `exercises/` | Five interactive exercise pages, one per objection (self-contained HTML + vanilla JS; real NOAA data embedded at build time). Linked from the “try it yourself” boxes in the explainer. |
| `CLAUDE.md` | Standing instructions and current state for Claude Code sessions in this repo (conventions, build, key numbers). |
| `NOTES.md` | Working notes: review of the original paper, accuracy audit, draft changelog. |
| `sources/` | The three primary documents (see `sources/README.md` — two are zip archives despite `.pdf` names). |
| `src/make_figures.py` | Generates all five figures. Replicates the L&S11 fit on real NOAA data and reproduces the Benestad et al. synthetic-noise experiment. |
| `src/extract_ls11_figures.py` | Crops L&S11's own figures (Figs. 1–5 and Fig. Sup. 1) from the arXiv preprint PDF for the explainer's "Working from the source paper to the rebuttal" section. |
| `src/casefile01_template.html` | Document source with `{{FIGn}}` placeholders. |
| `src/exercises/` | Exercise templates (`exN_*_template.html`) plus shared design-system CSS and math/chart JS, assembled by the build. |
| `src/build.py` | Regenerates figures, assembles the explainer, and builds the exercise pages. |
| `data/annual.csv` | NOAA NOAAGlobalTemp (GCAG) + NASA GISTEMP annual global anomalies, snapshot used for the current build. |
| `figures/` | Rendered PNGs (also embedded in the HTML). |

## Rebuilding

```bash
cd src
python3 build.py        # needs numpy, pandas, matplotlib, pymupdf
```

If your system Python lacks the dependencies, a repo-local venv works
(gitignored):

```bash
python3 -m venv ../../.venv && ../../.venv/bin/pip install numpy pandas matplotlib pymupdf
../../.venv/bin/python3 build.py
```

Deterministic: the synthetic-noise experiment uses a fixed seed (42). Outputs:
the explainer HTML, `figures/*.png`, and `exercises/*.html`. The exercise
pages embed the same `data/annual.csv` snapshot (injected as JSON at build
time); their in-browser fits reproduce the Python numbers exactly, except the
Exercise 3 noise experiment, which draws its own seeded random numbers in the
browser (recipe identical, RNG different — the page's footnote discloses
this).

## Data provenance

`data/annual.csv` is the "datasets/global-temp" mirror of NOAA NCEI
NOAAGlobalTemp (source `GCAG`, anomalies vs. the 20th-century mean, 1850–2025;
partial years excluded by the script) and NASA GISTEMP. To refresh:

```bash
curl -sL https://raw.githubusercontent.com/datasets/global-temp/main/data/annual.csv \
     -o data/annual.csv
```

Note: refreshing the data will shift the replication numbers slightly (the
document's methods note explains why, and treats dataset sensitivity as a
finding rather than a nuisance).

## Honest-labeling commitments

- Exhibits B, C, E use **real** NOAA data; Exhibit A is labeled schematic;
  Exhibit D is labeled synthetic and reproduces the method of the Benestad
  et al. supporting material.
- Numerical differences from the original paper (dataset vintage) are stated
  in the document, not hidden: e.g. residual ramp 0.81 °C/century here vs.
  their 0.66 ± 0.08 on 2010-vintage HadCRUT3.
- The synthetic-experiment inflation factor is construction-dependent
  (~14× here, ~4× in Benestad et al.); the document presents the instability
  as the finding, not the factor.

## Primary sources

- Loehle & Scafetta (2011), doi:10.2174/1874282301105010074 (arXiv:1206.5845)
- Benestad et al. (2016), doi:10.1007/s00704-015-1597-5 + supporting material
  ("Curve-fitting" section; Table S2; R package `replicationDemos`,
  function `LoehleScafetta2011()`)
