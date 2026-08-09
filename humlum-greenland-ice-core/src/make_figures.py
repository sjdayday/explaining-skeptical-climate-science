"""
Figures for: Case File 02 - Humlum, Solheim & Stordahl (2011) vs Benestad et al. (2016)
=======================================================================================
Fig 1  The whole file: ~50,000 years of GISP2, and the 4,000-year window used
Fig 2  Replication of the HSS11a-style fit inside the window (SM's demonstration)
Fig 3  The rebuttal's test: the fit extended into the discarded Holocene data
Fig 4  Where the record ends: the youngest sample is ~1855 CE

Data: GISP2 temperature reconstruction (Alley 2000/2004), NOAA NCEI file
data/gisp2_temp_accum_alley2000.txt — the same file cited by the Benestad
et al. supporting material (footnote 2, p. 5). Deterministic: no RNG.
"""

import os
import re

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

_here = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(_here, "..", "data", "gisp2_temp_accum_alley2000.txt")
OUT = os.path.join(_here, "..", "figures")
os.makedirs(OUT, exist_ok=True)

# ----------------------------------------------------------------------------- palette
INK    = "#1B2A3A"   # observations (the data the paper used)
CLAIM  = "#C7772E"   # amber: the HSS11a-style model
REBUT  = "#0E7C7B"   # teal: the rebuttal's demonstrations
GREY   = "#8A97A5"   # the discarded data
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
# Temperature section: file lines 76..1711 (0-indexed 75..1710), "age  temp".
rows = []
with open(DATA) as f:
    for i, line in enumerate(f):
        if i < 75:
            continue
        if i >= 1711:
            break
        m = re.match(r"\s*(\d+\.\d+)\s+(-?\d+\.\d+)\s*$", line)
        if m:
            rows.append((float(m.group(1)), float(m.group(2))))
age = np.array([a for a, _ in rows]) * 1000.0     # years before 1950 ("BP")
T = np.array([t for _, t in rows])
print(f"GISP2 temperature: n={len(T)}, {age.min():.0f}-{age.max():.0f} yr BP, "
      f"{T.min():.1f} to {T.max():.1f} degC; youngest sample = {1950 - age.min():.0f} CE")

# ----------------------------------------------------------------------------- model
PERIODS = (2804.0, 1186.0, 556.0)    # HSS11a's periods, as reported in the SM
CAL_MAX = 4000.0                     # their window: ages <= 4 kyr BP
HOLOCENE = 11700.0

def design(t, trend=True):
    cols = [np.ones_like(t)]
    if trend:
        cols.append(t)
    for P in PERIODS:
        w = 2 * np.pi / P
        cols += [np.sin(w * t), np.cos(w * t)]
    return np.column_stack(cols)

cal = age <= CAL_MAX
beta, *_ = np.linalg.lstsq(design(age[cal]), T[cal], rcond=None)
fit_cal = design(age[cal]) @ beta
r2_in = 1 - ((T[cal] - fit_cal) ** 2).sum() / ((T[cal] - T[cal].mean()) ** 2).sum()
rmse_in = float(np.sqrt(((T[cal] - fit_cal) ** 2).mean()))
amps = [float(np.hypot(beta[2 + 2 * i], beta[3 + 2 * i])) for i in range(3)]
print(f"Fit on ages<=4kyr (n={cal.sum()}): R2={r2_in:.3f}, RMSE={rmse_in:.2f} degC, "
      f"trend={beta[1] * 1000:+.3f} degC/kyr(toward past)")
print(f"  amplitudes 2804/1186/556 yr: {amps[0]:.3f}/{amps[1]:.3f}/{amps[2]:.3f} degC")

beta0 = beta.copy()
beta0[1] = 0.0                       # SM's second variant: trend zeroed

out = (age > CAL_MAX) & (age <= HOLOCENE)
for name, b in (("trend kept", beta), ("trend zeroed", beta0)):
    resid = T[out] - design(age[out]) @ b
    r2_out = 1 - (resid ** 2).sum() / ((T[out] - T[out].mean()) ** 2).sum()
    print(f"Extension 4-11.7 kyr ({name}): mean error={resid.mean():+.2f}, "
          f"RMSE={np.sqrt((resid ** 2).mean()):.2f} degC, R2={r2_out:.2f}")

# =========================================================== FIG 1 - the whole file
fig, ax = plt.subplots(figsize=(7.8, 3.9))
ax.axvspan(0, CAL_MAX / 1000, color="#FBF1E4", zorder=0)
ax.plot(age / 1000, T, color=INK, lw=0.8)
ax.axvline(CAL_MAX / 1000, color=CLAIM, lw=1.4, ls="--")
ax.annotate("the window the paper used:\nthe most recent 4,000 years\n(8% of the record's span)",
            xy=(2.0, -49), fontsize=8.5, color="#9A5A1F", ha="left")
ax.annotate("the rest of the same data file: ~46,000 years, not used",
            xy=(26, -33.2), fontsize=8.5, color=GREY, ha="center")
ax.annotate("youngest sample:\n≈1855 CE", xy=(age.min() / 1000, T[0]),
            xytext=(6.8, -34.8), fontsize=8,
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.9), color=INK)
ax.set_xlim(50, 0)
ax.set_xlabel("age (thousands of years before 1950)")
ax.set_ylabel("central Greenland temperature (°C)")
ax.set_title("One data file: the GISP2 temperature reconstruction, ~50,000 years",
             loc="left", fontsize=11.5, fontweight="bold", pad=8)
fig.savefig(OUT + "/fig1_record.png", bbox_inches="tight")
plt.close(fig)

# =========================================================== FIG 2 - inside the window
tt = np.linspace(age.min(), CAL_MAX, 1200)
fig, ax = plt.subplots(figsize=(7.6, 3.9))
ax.plot(age[cal] / 1000, T[cal], color=INK, lw=1.0, alpha=0.85,
        label="GISP2, most recent 4,000 years")
ax.plot(tt / 1000, design(tt) @ beta, color=CLAIM, lw=2.3,
        label=f"three fixed cycles (2,804 / 1,186 / 556 yr) + trend, fitted here — R² = {r2_in:.2f}")
ax.set_xlim(4, 0)
ax.set_xlabel("age (thousands of years before 1950)")
ax.set_ylabel("temperature (°C)")
ax.set_title("Inside the window, the three-cycle model fits well",
             loc="left", fontsize=11.5, fontweight="bold", pad=8)
ax.legend(loc="lower left", fontsize=8, frameon=False)
fig.savefig(OUT + "/fig2_window_fit.png", bbox_inches="tight")
plt.close(fig)

# =========================================================== FIG 3 - the reveal
th = np.linspace(age.min(), HOLOCENE, 3000)
mask_used = age <= CAL_MAX
mask_disc = (age > CAL_MAX) & (age <= HOLOCENE)
res_kept = T[out] - design(age[out]) @ beta
res_zero = T[out] - design(age[out]) @ beta0
fig, ax = plt.subplots(figsize=(7.8, 4.4))
ax.axvspan(0, CAL_MAX / 1000, color="#FBF1E4", zorder=0)
ax.plot(age[mask_disc] / 1000, T[mask_disc], color=GREY, lw=0.9,
        label="the discarded Holocene data (4–11.7 kyr)")
ax.plot(age[mask_used] / 1000, T[mask_used], color=INK, lw=1.0,
        label="the data they used (≤4 kyr)")
ax.plot(tt / 1000, design(tt) @ beta, color=CLAIM, lw=2.3, label="the fit, inside its window")
ext = th >= CAL_MAX
ax.plot(th[ext] / 1000, design(th[ext]) @ beta, color=CLAIM, lw=1.8, ls=(0, (5, 3)),
        label=f"same curve, extended (trend kept): RMSE {np.sqrt((res_kept**2).mean()):.1f} °C")
ax.plot(th[ext] / 1000, design(th[ext]) @ beta0, color=CLAIM, lw=1.8, ls=(0, (1, 2)),
        label=f"extended with trend zeroed: RMSE {np.sqrt((res_zero**2).mean()):.1f} °C")
ax.annotate(f"inside the window:\nRMSE {rmse_in:.1f} °C", xy=(2.0, -33.4),
            fontsize=8.5, color="#9A5A1F", ha="center")
ax.set_xlim(11.7, 0)
ax.set_ylim(-38.5, -28.5)
ax.set_xlabel("age (thousands of years before 1950)")
ax.set_ylabel("temperature (°C)")
ax.set_title("The rebuttal's test: extend the fit into the data the paper set aside",
             loc="left", fontsize=11.5, fontweight="bold", pad=8)
ax.legend(loc="lower center", fontsize=7.5, frameon=False, ncol=1)
fig.savefig(OUT + "/fig3_reveal.png", bbox_inches="tight")
plt.close(fig)

# =========================================================== FIG 4 - where it ends
recent = age <= 2000.0
fig, ax = plt.subplots(figsize=(7.6, 3.7))
yr_ce = 1950.0 - age[recent]
ax.plot(yr_ce, T[recent], color=INK, lw=1.1, label="GISP2, most recent 2,000 years")
ax.axvline(1950 - age.min(), color=REBUT, lw=1.4, ls="--")
ax.annotate("the record's youngest sample:\n≈1855 CE — the series stops here,\n"
            "before essentially all modern warming",
            xy=(1950 - age.min(), T[0]), xytext=(1290, -30.0), fontsize=8.5,
            arrowprops=dict(arrowstyle="->", color=REBUT, lw=1.1), color=INK)
ax.annotate('in this file, "present" (age 0)\n= 1950 by convention',
            xy=(2015, -32.1), fontsize=8, color=GREY, ha="right")
ax.set_xlim(-60, 2030)
ax.set_xlabel("year (CE)")
ax.set_ylabel("temperature (°C)")
ax.set_title("Where the record ends", loc="left", fontsize=11.5, fontweight="bold", pad=8)
ax.legend(loc="lower left", fontsize=8, frameon=False)
fig.savefig(OUT + "/fig4_endpoint.png", bbox_inches="tight")
plt.close(fig)

print("done")
