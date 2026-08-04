"""
Figures for: Case File 01 - Loehle & Scafetta (2011) vs Benestad et al. (2016)
==============================================================================
Fig 1  The "recipe": 60-yr wave + 20-yr wave + straight line = temperature-like curve
Fig 2  Replication of the L&S11 procedure on real NOAA data, seen from 2011
Fig 3  The rebuttal's stress test: phantom "60-year cycles" found in synthetic data
Fig 4  R-squared scan: is 60 years special? (period scan on the calibration data)
Fig 5  The out-of-sample test nature ran: the full L&S11 model vs 2011-2025 reality

Data: NOAAGlobalTemp (GCAG) annual anomalies vs 20th-century mean, 1850-2025,
via the open "datasets/global-temp" GitHub mirror (annual.csv).
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# ----------------------------------------------------------------------------- palette
INK    = "#1B2A3A"   # deep ink navy: text, observations
CLAIM  = "#C7772E"   # amber: the L&S11 model / claim side
REBUT  = "#0E7C7B"   # teal: the rebuttal's demonstrations
GREY   = "#8A97A5"   # supporting grey
PAPER  = "#FFFFFF"

mpl.rcParams.update({
    "figure.dpi": 160, "savefig.dpi": 160, "savefig.facecolor": PAPER,
    "figure.facecolor": PAPER, "axes.facecolor": PAPER,
    "font.family": "DejaVu Sans", "font.size": 9.5,
    "axes.edgecolor": INK, "axes.labelcolor": INK, "text.color": INK,
    "xtick.color": INK, "ytick.color": INK,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": "#DDE4EA", "grid.linewidth": 0.6,
})

# ----------------------------------------------------------------------------- data
df = pd.read_csv("annual.csv")
g = df[(df.Source == "GCAG") & (df.Year <= 2025)].sort_values("Year")
yr = g.Year.to_numpy(dtype=float)
T  = g.Mean.to_numpy(dtype=float)
print(f"GCAG: {yr.min():.0f}-{yr.max():.0f}, n={len(yr)}")

def design(t, periods=(60.0, 20.0), trend=True):
    """Design matrix: [1, t, sin/cos pairs]  (t in years)."""
    cols = [np.ones_like(t)]
    if trend:
        cols.append(t - 1900.0)
    for P in periods:
        w = 2 * np.pi / P
        cols += [np.sin(w * t), np.cos(w * t)]
    return np.column_stack(cols)

def fit(t, y, periods=(60.0, 20.0), trend=True):
    X = design(t, periods, trend)
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    return beta

def predict(beta, t, periods=(60.0, 20.0), trend=True):
    return design(t, periods, trend) @ beta

def amp(beta, i_pair, trend=True):
    """Amplitude of the i-th sin/cos pair."""
    k = (2 if trend else 1) + 2 * i_pair
    return float(np.hypot(beta[k], beta[k + 1]))

def r2(y, yhat):
    ss = np.sum((y - np.mean(y)) ** 2)
    return 1.0 - np.sum((y - yhat) ** 2) / ss

# =========================================================== L&S11-style calibration
cal = yr <= 1950
beta = fit(yr[cal], T[cal])
nat_full = predict(beta, yr)                       # natural-only model, all years
print(f"Calibration 1850-1950:  R2={r2(T[cal], predict(beta, yr[cal])):.3f}")
print(f"  60-yr amplitude={amp(beta,0):.3f} degC   20-yr amplitude={amp(beta,1):.3f} degC")
print(f"  linear term={beta[1]*100:.3f} degC/century")

# residual after natural model; their anthropogenic ramp
res = T - nat_full
post = (yr >= 1951) & (yr <= 2010)
pr = np.polyfit(yr[post], res[post], 1)
print(f"Residual trend 1951-2010: {pr[0]*100:.2f} degC/century  (L&S11: 0.66 +/- 0.08)")

# zero-crossing year of the residual ramp (L&S11 say ~1942)
t0 = -pr[1] / pr[0]
print(f"Residual ramp crosses zero at ~{t0:.0f}  (L&S11: 1942)")

def full_model(t):
    """L&S11 'full natural + anthropogenic' model, re-derived on this data:
    cycles-and-line calibrated 1850-1950, plus the straight ramp fitted to the
    1951-2010 residuals (their 'anthropogenic' component), extended forward."""
    ramp = np.clip(np.polyval(pr, t), 0, None)
    return predict(beta, t) + ramp
print(f"Full-model mean misfit 1951-2010: {np.mean(T[post]-full_model(yr[post])):+.3f} degC")

# =========================================================== FIG 1 - the recipe
t1 = np.arange(1850, 2011.0)
w60 = 0.11 * np.sin(2 * np.pi * (t1 - 1910) / 60.0)
w20 = 0.035 * np.sin(2 * np.pi * (t1 - 1902) / 20.0)
lin = 0.0045 * (t1 - 1850) - 0.35
tot = w60 + w20 + lin

fig, axs = plt.subplots(4, 1, figsize=(7.4, 5.4), sharex=True,
                        gridspec_kw=dict(height_ratios=[1, 1, 1, 1.55], hspace=0.42))
parts = [(w60, CLAIM, 'a 60-year wave'), (w20, CLAIM, 'a 20-year wave'),
         (lin, GREY, 'a gentle straight line')]
for ax, (yv, c, lab) in zip(axs[:3], parts):
    ax.plot(t1, yv, color=c, lw=2)
    ax.set_ylim(-0.55, 0.55); ax.set_yticks([])
    ax.text(1853, 0.38, lab, fontsize=10, color=INK, fontweight="bold")
    ax.grid(False)
axs[0].set_title("The claim's recipe: add three simple ingredients \u2026", loc="left",
                 fontsize=11.5, fontweight="bold", pad=8)
axs[3].plot(t1, tot, color=INK, lw=2.2)
axs[3].set_ylim(-0.75, 0.75); axs[3].set_yticks([])
axs[3].text(1853, 0.5, "\u2026 and the sum looks a lot like the global temperature record",
            fontsize=10, color=INK, fontweight="bold")
axs[3].grid(False)
for ax, sym in zip(axs[:3], ["+", "+", "="]):
    ax.annotate(sym, xy=(0.5, -0.32), xycoords="axes fraction", fontsize=15,
                fontweight="bold", color=GREY, ha="center")
axs[3].set_xlabel("year")
fig.savefig("fig1_recipe.png", bbox_inches="tight")
plt.close(fig)

# =========================================================== FIG 2 - the 2011 view
m2010 = yr <= 2010
fig, (a, b) = plt.subplots(2, 1, figsize=(7.6, 6.0), sharex=True,
                           gridspec_kw=dict(height_ratios=[2.1, 1.15], hspace=0.16))
a.axvspan(1850, 1950, color="#EDF2F6", zorder=0)
a.plot(yr[m2010], T[m2010], color=INK, lw=1.1, alpha=0.85, label="observed global temperature (NOAA)")
a.plot(yr[cal], predict(beta, yr[cal]), color=CLAIM, lw=2.4, label="cycles + line, fitted 1850\u20131950")
ext = (yr > 1950) & m2010
a.plot(yr[ext], nat_full[ext], color=CLAIM, lw=2.4, ls=(0, (5, 3)),
       label="same curve, extended 1951\u20132010")
a.text(1897, 0.62, "fitting window\n1850\u20131950", fontsize=8.5, color=GREY, ha="center")
a.annotate("the wiggles line up:\n1940s bump, 1970s dip, 2000s crest",
           xy=(1999, nat_full[yr == 1999][0]), xytext=(1958, 0.75), fontsize=8.5,
           arrowprops=dict(arrowstyle="-", color=GREY, lw=0.9), color=INK)
a.set_ylabel("temperature anomaly (\u00b0C)")
a.legend(loc="upper left", fontsize=8, frameon=False)
a.set_title("What Loehle & Scafetta did \u2014 re-created here with real NOAA data, as of 2010",
            loc="left", fontsize=11.5, fontweight="bold", pad=8)

b.axvspan(1850, 1950, color="#EDF2F6", zorder=0)
b.plot(yr[m2010], res[m2010], color=GREY, lw=1.0, label="what's left after removing the cycles")
tt = np.arange(1942, 2011.0)
b.plot(tt, np.polyval(pr, tt), color=CLAIM, lw=2.4,
       label=f"straight line from 1942: \u2248{pr[0]*100:.2f} \u00b0C/century")
b.axhline(0, color=GREY, lw=0.7)
b.text(1946, -0.28, 'their claimed human share:\na modest ramp starting ~1942', fontsize=8.5, color=INK)
b.set_xlabel("year"); b.set_ylabel("residual (\u00b0C)")
b.legend(loc="upper left", fontsize=8, frameon=False)
b.set_xlim(1850, 2012)
fig.savefig("fig2_replication_2011.png", bbox_inches="tight")
plt.close(fig)

# =========================================================== FIG 3 - phantom cycles
N = 10_000
tsyn = np.arange(N, dtype=float)
K = 400
periods = np.exp(rng.uniform(np.log(3), np.log(3000), K))
amps    = rng.uniform(0, 1, K)
phases  = rng.uniform(0, 2 * np.pi, K)
syn = sum(A * np.sin(2 * np.pi * tsyn / P + ph) for A, P, ph in zip(amps, periods, phases))

# scale the synthetic series so its variability matches the real 1850-2010 record
# (after removing the linear trend), so amplitudes are directly comparable
m160 = (yr >= 1850) & (yr <= 2010)
obs_detr = T[m160] - np.polyval(np.polyfit(yr[m160], T[m160], 1), yr[m160])
syn = (syn - syn.mean()) / syn.std() * obs_detr.std()
print(f"Detrended real-record std 1850-2010: {obs_detr.std():.3f} degC (synthetic scaled to match)")

# same estimator applied to the real 160-year record: its apparent 60-yr strength
beta160 = fit(yr[m160], T[m160])
amp60_real = amp(beta160, 0)
print(f"Real record 1850-2010, same fit: 60-yr amplitude = {amp60_real:.3f} degC")

seg_len = 160
nseg = N // seg_len
amps60, fits = [], []
for i in range(nseg):
    ts = tsyn[i * seg_len:(i + 1) * seg_len]
    ys = syn[i * seg_len:(i + 1) * seg_len]
    bb = fit(ts, ys)
    amps60.append(amp(bb, 0))
    fits.append((ts, ys, predict(bb, ts)))
amps60 = np.array(amps60)
beta_all = fit(tsyn, syn)
amp_all = amp(beta_all, 0)
print(f"Synthetic: full-series 60-yr amplitude={amp_all:.4f}; "
      f"segment mean={amps60.mean():.4f}  (ratio {amps60.mean()/amp_all:.1f}x), "
      f"range {amps60.min():.3f}-{amps60.max():.3f}")

fig = plt.figure(figsize=(7.6, 6.2))
gs = fig.add_gridspec(2, 2, height_ratios=[1.05, 1], hspace=0.5, wspace=0.25)

axA = fig.add_subplot(gs[0, :])
jitter = rng.uniform(-0.16, 0.16, nseg)
axA.scatter(np.arange(1, nseg + 1) + jitter * 0, amps60, s=26, color=REBUT, zorder=3,
            label='apparent "60-year cycle" strength in each slice')
axA.axhline(amps60.mean(), color=REBUT, lw=1.2, ls=":",
            label=f"average across slices ({amps60.mean():.2f} \u00b0C)")
axA.axhline(amp_all, color=INK, lw=1.6,
            label=f"true 60-yr strength of the whole series ({amp_all:.2f} \u00b0C)")
axA.axhline(amp60_real, color=CLAIM, lw=1.6, ls="--",
            label=f"for scale: 60-yr strength the same fit finds in the REAL record ({amp60_real:.2f} \u00b0C)")
axA.set_xlabel(f"slice number  (each slice = {seg_len} 'years' of the same random series)")
axA.set_ylabel("fitted amplitude (\u00b0C)")
axA.set_title("The stress test: slice 10,000 years of structured randomness into 160-year pieces",
              loc="left", fontsize=11.5, fontweight="bold", pad=8)
axA.legend(fontsize=8, frameon=False, loc="upper right")
axA.set_ylim(0, max(amps60.max(), 0.3) * 1.15)

pick = [int(np.argmax(amps60)), int(np.argsort(amps60)[-6])]
for k, (axpos, idx) in enumerate(zip([gs[1, 0], gs[1, 1]], pick)):
    ax = fig.add_subplot(axpos)
    ts, ys, yh = fits[idx]
    ax.plot(ts - ts[0], ys, color=GREY, lw=0.9, label="random data")
    ax.plot(ts - ts[0], yh, color=REBUT, lw=2.2, label='fitted "cycles"')
    ax.set_title(f'slice {idx+1}: a convincing-looking "cycle"', fontsize=9.5)
    ax.set_xlabel("'year' within slice")
    if k == 0:
        ax.set_ylabel("value (\u00b0C)")
        ax.legend(fontsize=7.5, frameon=False, loc="lower left")
fig.savefig("fig3_phantom_cycles.png", bbox_inches="tight")
plt.close(fig)

# =========================================================== FIG 4 - is 60 special?
P1s = np.arange(30, 100.1, 0.25)
r2s = []
for P1 in P1s:
    bb = fit(yr[cal], T[cal], periods=(P1, 20.0))
    r2s.append(r2(T[cal], predict(bb, yr[cal], periods=(P1, 20.0))))
r2s = np.array(r2s)
best = P1s[np.argmax(r2s)]
r2_60 = r2s[np.argmin(np.abs(P1s - 60))]
print(f"Period scan on 1850-1950: best long period={best:.2f} yr (R2={r2s.max():.3f}); "
      f"R2 at 60 yr={r2_60:.3f}")

fig, ax = plt.subplots(figsize=(7.4, 3.4))
ax.plot(P1s, r2s, color=REBUT, lw=2)
ax.axvline(60, color=CLAIM, lw=1.6, ls="--")
ax.text(60.7, ax.get_ylim()[0] + 0.02, "the chosen 60 yr", color=CLAIM, fontsize=8.5,
        rotation=90, va="bottom")
ax.scatter([best], [r2s.max()], color=INK, zorder=3)
ax.annotate(f"best fit here: {best:.0f} yr", xy=(best, r2s.max()),
            xytext=(best + 4, r2s.max() - 0.06), fontsize=8.5,
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.9))
ax.set_xlabel("assumed long period (years), with the short period held at 20 yr")
ax.set_ylabel("goodness of fit (R\u00b2), 1850\u20131950")
ax.set_title("Is 60 years special? Many periods fit the calibration data about equally well",
             loc="left", fontsize=11.5, fontweight="bold", pad=8)
fig.savefig("fig4_period_scan.png", bbox_inches="tight")
plt.close(fig)

# =========================================================== FIG 5 - the verdict of time
tproj = np.arange(1850, 2036.0)
fm = full_model(tproj)
fig, ax = plt.subplots(figsize=(7.6, 4.6))
ax.axvspan(2011, 2035, color="#EDF2F6", zorder=0)
ax.plot(yr, T, color=INK, lw=1.3, label="observed global temperature (NOAA, to 2025)")
ax.plot(tproj, fm, color=CLAIM, lw=2.4, ls=(0, (5, 3)),
        label=f"full L&S11-style model: cycles + straight human ramp ({pr[0]*100:.1f} \u00b0C/century)")
ax.axvline(2011, color=GREY, lw=1.0)
ax.text(2011.6, -0.42, "paper\npublished", fontsize=8, color=GREY)
i24 = int(np.where(yr == 2024)[0][0])
gap = T[i24] - full_model(np.array([2024.0]))[0]
ax.annotate(f"2024: reality is\n\u2248{gap:.1f} \u00b0C above the model",
            xy=(2024, T[i24]), xytext=(1978, 1.12), fontsize=9, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
ax.text(2013, 0.06, "model says the cycle's\ndownswing keeps things flat", fontsize=8.5,
        color=CLAIM)
ax.set_xlabel("year"); ax.set_ylabel("temperature anomaly (\u00b0C)")
ax.set_title("The out-of-sample test nature ran: 2011\u20132025", loc="left",
             fontsize=11.5, fontweight="bold", pad=8)
ax.legend(loc="upper left", fontsize=8, frameon=False)
ax.set_xlim(1850, 2036)
fig.savefig("fig5_aftermath.png", bbox_inches="tight")
plt.close(fig)

print("done")
