# Working notes — Case File 02

## Source inventory (2026-08-09)

**In hand:**
1. **Benestad et al. (2016) SM**, "Selective use of data" section (root
   `../sources/benestadetalnccSM2014.pdf`, zip container; the HSS11a case is
   pages 5–8; Figure S1 legend p. 57; Table S1 entry p. 62). Gives: the
   three periods (2,804, 1,186, 556 yr; and for Svalbard 68.4, 25.7,
   16.8 yr); HSS11a's own stated reason for the 4,000-yr window ("chose to
   focus on the most recent 4000 years of the GISP2 series, as the main
   thrust of [their] investigation is on climatic variations in the recent
   past and their potential for forecasting the near future"); their claims
   to "produce testable forecasts of future climate" and a "realistic
   forecasting time range of about 10–25% of the total record length"; the
   Bye et al. (2011) point (Humlum co-authored a popular article showing
   the discarded part of the same data); the data-file footnote (the NOAA
   file now in `data/`); Figure S1's two extension variants; the physics
   objection (sun/moon inactive before 4 kyr BP?); wavelet end-point
   sensitivity; category B-or-D classification.
2. **Solheim, Stordahl & Humlum (2011/2012)**, "Solar Activity and Svalbard
   Temperatures" (`sources/`, true PDF, 8 pp.). Same author cluster; its
   ref. [3] is HSS11a (with Svalbard periods 62–68/26/15–17 yr and trend
   0.023 °C/yr quoted); predicts Svalbard annual-mean **−3.5 ± 2 °C** for
   solar cycle 24 (2009–20) and winter ≈ −6 °C, from a solar-cycle-length
   model claiming 60% of variance explained. The falsifiable forecast for
   Part Three.
3. **GISP2 data** (`data/`, fetched 2026-08-09 from NOAA NCEI). Verified:
   1,631 temperature samples, 0.0951–49.981 kyr BP (ages before 1950);
   youngest sample ≈1855 CE; ≤4 kyr window = 395 samples = 24% of samples,
   8% of time span; temperature range −53.6…−28.7 °C.
4. **ESDD open review** (Case 01's `sources/esdd-open-review/` roster):
   C257 = Solheim, Humlum, Stordahl & Yndestad's defense (not yet
   extracted — fetch when drafting the defenses section); C304 = Matthews'
   Dirichlet correction. Verified 2026-08-09: the final SM does **not**
   repeat the Dirichlet claim (grep "Dirichlet" over all SM pages: no hits) —
   it instead cites Stephenson/Williams/Pain on Fourier series being valid
   only within the fitted interval. The Matthews flag from Case 01 is
   resolved: the misstatement did not survive into the 2016 SM.

**Missing / wanted:**
- **HSS11a itself**: Humlum, Solheim & Stordahl (2011), "Identifying natural
  contributions to late Holocene climate change," Global and Planetary
  Change 79:145–156, doi:10.1016/j.gloplacha.2011.09.005. Paywalled
  (Elsevier). Needed for the steel-man's own numbers (their variance-
  explained figures, their Fig. 5 forecast curve, the exact wavelet method)
  and for a "Working from the source paper" section. **Ask Steve to supply
  the PDF into `sources/`** (as he did for L&S11).
- C257 extracted text (URL pattern in the Case 01 esdd-open-review README).
- Svalbard Airport observed temperatures through solar cycle 24 (for the
  forecast-verification exhibit): candidate sources — Norwegian MET
  (seklima), NASA GISS station data (Svalbard Lufthavn). Not yet fetched.

## Replication (prototype 2026-08-09, now in make_figures.py)

SM-style fit: constant + linear trend + 3 sinusoids with periods fixed at
2,804/1,186/556 yr, least squares on ages ≤ 4 kyr BP (395 points):
- In-window: R² 0.852, RMSE 0.30 °C; trend +0.445 °C/kyr (increasing with
  age = late-Holocene cooling toward the record's 1855 end); amplitudes
  0.319/0.467/0.272 °C.
- Extended to the rest of the Holocene (4–11.7 kyr BP): mean error
  −3.22 °C, RMSE 4.45 °C, out-of-window R² −2.9 (trend kept). Trend zeroed
  (SM's second variant): mean error +0.20 °C, RMSE 2.39 °C.
- Framing per precision norms: the fair test is the Holocene comparison
  (same climate state); the glacial section is context, not the test.

## Draft changelog

### Draft 1 (2026-08-09)
- Directory scaffolded on the Case 01 model; GISP2 data fetched and
  verified; SM account extracted and read in full; Svalbard companion PDF
  read; replication built (numbers above); case file drafted with four
  objections + aftermath; figures A–D.
- Not yet present (deliberately): interactive exercises; "Working from the
  source paper" section; the ESDD defenses section (C257); the Svalbard
  forecast-verification exhibit with observed data; Going-deeper links.
  All blocked on, or deferred behind, the missing primary PDF and a
  Svalbard data fetch.

## Open items
- Obtain HSS11a PDF → then: steel-man from their own text; from-the-source
  section; check our replication numbers against their reported fit.
- Fetch C257, draft "defenses, answered" section.
- Fetch Svalbard observations; verify the −3.5 ± 2 °C forecast outcome
  quantitatively; add the exhibit.
- Exercises (candidates): (1) "choose your window" — slide a 4,000-yr
  window along the full record, fit, and watch the "cycles" change;
  (2) "the reveal" — fit in-window, then uncover the discarded era
  (curtain mechanic from Case 01 Ex 4 transfers directly); (3) periods
  dial like Case 01 Ex 2.
- Consider an Exhibit comparing sample coverage: 4,000 of 49,980 years
  (8%) vs the paper's "10–25% of the total record length" forecasting
  claim — their own rule applied to the full file would allow a
  5,000–12,500-yr forecast horizon, which their fit demonstrably cannot
  survive even 7,700 years back.
