# Sources

Primary documents for Case File 01, as provided to the project.

| File | Format | Contents |
|---|---|---|
| `loehlescafetta1206_5845v1.pdf` | true PDF (47 pp.) | Loehle & Scafetta (2011) arXiv preprint 1206.5845v1, incl. Table 1 and Supplemental Information 1–3 |
| `../../sources/benestadetal2016-learning-from-mistakes.pdf` (moved to repo root) | true PDF (5 pp.) | Benestad et al. (2016), main paper, "Learning from mistakes in climate research", Theor. Appl. Climatol. 126:699–703, doi:10.1007/s00704-015-1597-5, CC BY 4.0. Replaces an earlier zip-container file of the same pages; re-downloaded 2026-10-14 from the Texas Tech ThinkTech repository copy (hdl:2346/92619), library cover sheet removed. Shared across case files. |
| `../../sources/benestadetalnccSM2014.pdf` (moved to repo root) | true PDF (81 pp.) | Supporting material "Learning through replication in climate research"; "Curve-fitting" section is on pages ~9–11; Table S3 (pp. 64–67) is image-only. Shared across case files since Case 02. |
| `esdd-open-review/` | extracted texts (CC BY 3.0) | The 2013 ESDD public-review defenses of L&S11 and replies (Loehle C253, Benestad C258, Scafetta C318, Matthews C304), plus a roster README with the full comment list and PDF URL pattern. The case file's "Four defenses, four answers" section answers these; keep them in sync. |
| `replicationDemos-resonance.R` | R source (GPL ≥ 2) | Archived from github.com/brasmus/replicationDemos: `resonance()`/`FOscillator()`/`resonanceTest()`, the forced-damped-oscillator demonstration behind the SM's resonance passage and the case file's Exhibit F. The shipped driver halts at a stray `stop()` (line 120) before its sinusoid/noise/CO₂ panels. |
| `replicationDemos-FT.R` | R source (GPL ≥ 2) | Archived from the same repo: `decomposeFT()`, the structured-noise recipe (50 harmonics, Gaussian random amplitudes weighted 1/√i) used by `resonance.R` and mirrored by Exhibit F's rows A–B. |

These are working copies for reference during drafting. If you prefer not to
version reference documents, add `sources/` to `.gitignore`.
