"""
Build the Case File 01 explainer.

  1. Runs make_figures.py, which reads ../data/annual.csv and writes five PNGs
     to ../figures/.
  2. Injects the PNGs (base64) into casefile01_template.html.
  3. Writes the self-contained document to
     ../casefile01-loehle-scafetta-curve-fitting.html

Usage:  cd src && python3 build.py
Deps:   numpy, pandas, matplotlib
"""

import base64
import pathlib
import runpy

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

print("1/2  Generating figures ...")
runpy.run_path(str(HERE / "make_figures.py"), run_name="__main__")

print("2/2  Assembling HTML ...")
tpl = (HERE / "casefile01_template.html").read_text()
figures = {
    1: "fig1_recipe",
    2: "fig2_replication_2011",
    3: "fig3_phantom_cycles",
    4: "fig4_period_scan",
    5: "fig5_aftermath",
}
for i, name in figures.items():
    png = (ROOT / "figures" / f"{name}.png").read_bytes()
    tpl = tpl.replace("{{FIG%d}}" % i,
                      "data:image/png;base64," + base64.b64encode(png).decode())
assert "{{FIG" not in tpl, "unreplaced figure placeholder"

out = ROOT / "casefile01-loehle-scafetta-curve-fitting.html"
out.write_text(tpl)
print(f"done: {out}  ({out.stat().st_size/1e6:.1f} MB)")
