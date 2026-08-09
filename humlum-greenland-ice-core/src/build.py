"""
Build the Case File 02 explainer.

  1. Runs make_figures.py, which reads ../data/gisp2_temp_accum_alley2000.txt
     and writes four PNGs to ../figures/.
  2. Injects the PNGs (base64) into casefile02_template.html and writes the
     self-contained document to ../casefile02-humlum-greenland-ice-core.html

Usage:  cd src && python3 build.py
Deps:   numpy, matplotlib
"""

import base64
import pathlib
import runpy

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

print("1/2  Generating figures ...")
runpy.run_path(str(HERE / "make_figures.py"), run_name="__main__")

print("2/2  Assembling HTML ...")
tpl = (HERE / "casefile02_template.html").read_text()
figures = {
    "FIG1": "fig1_record",
    "FIG2": "fig2_window_fit",
    "FIG3": "fig3_reveal",
    "FIG4": "fig4_endpoint",
}
for key, name in figures.items():
    png = (ROOT / "figures" / f"{name}.png").read_bytes()
    tpl = tpl.replace("{{%s}}" % key,
                      "data:image/png;base64," + base64.b64encode(png).decode())
assert "{{FIG" not in tpl, "unreplaced figure placeholder"

out = ROOT / "casefile02-humlum-greenland-ice-core.html"
out.write_text(tpl)
print(f"done: {out}  ({out.stat().st_size / 1e6:.1f} MB)")
