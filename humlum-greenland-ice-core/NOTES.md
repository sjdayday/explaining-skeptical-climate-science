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

5. **HSS11a itself** (`sources/Identifying_natural_contributions_to_late_
   Holocene.pdf`, true PDF, 12 pp., supplied by Steve 2026-08-10; replaced
   the Svalbard PDF, which was restored from git history — both now
   present). Full review below.

**Missing / wanted:**
- C257 extracted text (URL pattern in the Case 01 esdd-open-review README).
- Svalbard Airport observed temperatures through solar cycle 24 (for the
  forecast-verification exhibit): candidate sources — Norwegian MET
  (seklima), NASA GISS station data (Svalbard Lufthavn). Not yet fetched.

## Review of the primary paper (added to project 2026-08-10)

Read in full; draft 2 incorporates it. Numbered points mirror Case 01's
review style. PDF page N = printed page 144+N; cite printed pages.

1. **Program.** "An empirical bottom-up approach to climate modelling"
   (p. 145): Fourier spectrum + Morlet continuous wavelet transform
   (AutoSignal v1.7, SeaSolve; Torrence & Compo algorithms; wave number
   10), then a 3-stage sinusoidal model: Fourier for frequencies → linear
   fit for amplitudes/phases → nonlinear optimization. Detrend before,
   retrend after — **the linear trend is assumed to continue** through any
   forecast (stated in the Fig. 4 and Fig. 5 captions).
2. **Svalbard record** (1912–2010, composite of 4 stations): trend
   0.23 °C/decade, flagged by the authors themselves as possibly
   "unrealistic high" (record starts cold, ends warm). Fourier: 68.4,
   25.7, 16.8 yr (amps > 0.8 °C; 68.4 > 99.9% vs white noise). Wavelet
   adds 83, 62, 36, 12.5–11.6, 8.8 yr.
3. **Svalbard models.** Truncated 1912–1990: periods 71.7/24.9/15.3,
   r² = 0.36 (N=78) vs 0.02 linear; the 1991–2010 out-of-sample test (26%
   of truncated length) tracks the withheld years incl. warm 2005–2007 —
   their strongest card, steel-manned in Part One. Full 1912–2010: periods
   74.3/24.5/17.1, r² = 0.47 vs 0.14 linear. Forecast: decline to
   2015–2017, minor peak ~2026; "the observed late 20th century warming in
   Svalbard is not going to continue for the next 20–25 years" (p. 152);
   falsification timescale ~7 yr (9 yr for the truncated model).
4. **The 10–25% rule** (pp. 151, 155): "realistic forecasting time range of
   about 10–25% of the total record length," from truncation tests on
   meteorological series. Applied to the 4,000-yr GISP2 window this
   licenses 400–1,000-yr extensions — the basis for our new 4–5 kyr BP
   diagnostic band (RMSE 1.66/1.02 °C vs 0.30 in-window).
5. **GISP2 window choice** (pp. 145–146): the full quote has TWO reasons —
   recent-past focus (the one the SM quoted) AND "this part of the GISP2
   series shows an overall linear temperature trend, which simplifies the
   following analysis." The second is new to draft 2 and sharpens
   Objection 1: the window was selected partly for being model-friendly.
6. **GISP2 analysis** (pp. 152–154): resolution ~20 yr; ends 1855 AD
   (stated); detrended −0.0052 °C/decade; Fourier peaks 3598, 1139, 788,
   584, 366 yr (all > 99.9% vs white noise); wavelet 3500, 1170–1130,
   790–770, 590–560, 390–360 yr. **Model periods 2804/1186/556 by
   nonlinear optimization — 2804 is not a spectral peak (3598 is), and is
   70% of the window length (1.4 repeats).** r² = 0.63. Reproduces
   Minoan/Roman/Medieval warm periods, Dark Age, LIA; admits missing the
   3–400 AD warming. No 1470-yr Bond cycle found (discussed, Schulz cited).
7. **Their out-of-sample claim** (p. 154): the extension "is able to
   forecast the observed 1856–2010 warming (Fig. 8) as an out-of-sample
   forecasting test" — 155 yr ≈ 4% of record. Answered in Objection 2:
   shortest model period is 556 yr, so this "forecast" is only the long
   cycles' upswing at the window edge; meanwhile 7,700 yr of same-epoch
   data sat in the file.
8. **Mechanism** (pp. 148–150): lunar-tidal hypothesis chain (8.85-yr
   apsides, 18.6-yr nodal cycle + Yndestad's Barents Sea harmonics 55.8,
   74.4 yr; "We hypothesise that this may bring about the emergence of
   relatively warm or cold water masses..."); solar De Vries ~205 yr and
   Hallstatt ~2300 yr for GISP2; but "the attribution of physical
   explanations for the observed cyclic climate change is not our main
   concern" (p. 153).
9. **Representativeness caveats stated in-paper** (p. 154): Greenland "not
   identical to global temperature changes" but "tend[s] to reflect
   planetary temperature changes with a decadal-scale delay" (Chylek &
   Lohmann 2005; Brox et al. 2009 — the citation "Brox" appears to be Box
   et al.'s Greenland series, sic in the paper); Antarctic roughly
   anti-phased. Objection 5 now credits the candour and targets the gap
   between caveats and conclusions.
10. **Conclusions** (pp. 154–155): (2) post-LIA warming "to a high degree
    may be the result of natural climatic variations"; (3) warm period
    continues "for most of the 21st century," then late-Holocene cooling,
    "dependant [sic] on the magnitude of the anthropogenic greenhouse
    enhancement." NOTE the Greenland forecast is continued WARMTH — draft
    1's dossier/table said "natural cooling ahead," corrected in draft 2.
    The falsified cooling forecasts are the Svalbard ones.
11. **r² reconciliation.** Their 0.63 (wavelet-guided nonlinear optimization,
    detrend/retrend construction) vs our 0.852 (least squares, trend fitted
    jointly, their periods imposed): construction differs; both support
    "fits well in-window." Disclosed in Exhibit A's caption and methods.

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

### Draft 2 (2026-08-10) — checked against the original paper
- Primary PDF received; every draft-1 claim about HSS11a re-verified against
  it (all held up); SM-quoted passages replaced with direct quotations
  (journal page cites); status/meta bumped.
- Part One rebuilt from the paper: the bottom-up program, both records'
  machinery and numbers (Svalbard r² 0.36/0.47 + the 1991–2010 truncation
  test steel-manned as their strongest card), the full two-reason window
  quote, GISP2 Fourier peaks vs optimized periods, r² 0.63, mechanism
  chain, in-paper caveats moved into "Why it persuaded people."
- Corrections from the primary: the GISP2 forecast is continued warmth for
  most of the 21st century (draft 1 implied cooling — fixed in dossier and
  table); the falsified cooling forecasts are Svalbard's (this paper:
  decline to 2015–17; companion: −3.5 ± 2 °C over SC24).
- Objections sharpened: Obj 1 adds the "simplifies the following analysis"
  window reason; Obj 2 answers their claimed 1856–2010 out-of-sample
  success and adds the new within-their-own-rule diagnostic (4–5 kyr BP:
  RMSE 1.66/1.02 °C vs 0.30 in-window — 3–5× worse inside their claimed
  validity range); Obj 3 adds 2804 = 70% of window (1.4 repeats) and
  2804-not-a-spectral-peak (3598 is); Obj 5 credits the paper's stated
  caveats and targets the caveat→conclusion gap.
- make_figures.py: new 4–5 kyr band diagnostic; Exhibit C caption updated.
- sources/: primary PDF added (Steve); Svalbard companion restored from git
  history after the swap; sources/README rewritten.

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
- "Working from the source paper to the rebuttal" section (Case 01 model):
  quotes are in place from draft 2; still needs the paper's own figures
  cropped from the PDF (their Figs. 6–8 especially — spectrum, wavelet
  diagram, the model+forecast figure) via an extract script like Case 01's.
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
