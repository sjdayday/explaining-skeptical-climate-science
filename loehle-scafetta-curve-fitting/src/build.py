"""
Build the Case File 01 explainer and its interactive exercises.

  1. Runs make_figures.py, which reads ../data/annual.csv and writes five PNGs
     to ../figures/.
  2. Injects the PNGs (base64) into casefile01_template.html and writes the
     self-contained document to ../casefile01-loehle-scafetta-curve-fitting.html
  3. Builds the five interactive exercise pages from src/exercises/ templates,
     injecting the shared CSS/JS and the real GCAG data (JSON), and writes them
     to ../exercises/.

Usage:  cd src && python3 build.py
Deps:   numpy, pandas, matplotlib
"""

import base64
import csv
import json
import pathlib
import runpy

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

print("1/3  Generating figures ...")
runpy.run_path(str(HERE / "make_figures.py"), run_name="__main__")
runpy.run_path(str(HERE / "extract_ls11_figures.py"), run_name="__main__")

print("2/3  Assembling HTML ...")
tpl = (HERE / "casefile01_template.html").read_text()
figures = {
    "FIG1": "fig1_recipe",
    "FIG2": "fig2_replication_2011",
    "FIG3": "fig3_phantom_cycles",
    "FIG4": "fig4_period_scan",
    "FIG5": "fig5_aftermath",
    "LS11FIG1": "ls11_fig1",
    "LS11FIG2": "ls11_fig2",
    "LS11FIG3": "ls11_fig3",
    "LS11FIG4": "ls11_fig4",
    "LS11FIG5": "ls11_fig5",
    "LS11FIGSUP1": "ls11_figsup1",
}
for key, name in figures.items():
    png = (ROOT / "figures" / f"{name}.png").read_bytes()
    tpl = tpl.replace("{{%s}}" % key,
                      "data:image/png;base64," + base64.b64encode(png).decode())
assert "{{FIG" not in tpl and "{{LS11" not in tpl, "unreplaced figure placeholder"

out = ROOT / "casefile01-loehle-scafetta-curve-fitting.html"
out.write_text(tpl)
print(f"done: {out}  ({out.stat().st_size/1e6:.1f} MB)")

print("3/3  Building exercises ...")
EX = HERE / "exercises"
shared_css = (EX / "_shared.css").read_text()
shared_js = (EX / "_shared.js").read_text()

# GCAG annual anomalies (same series the figures use), compact JSON
with open(ROOT / "data" / "annual.csv") as f:
    rows = [r for r in csv.DictReader(f)
            if r["Source"] == "GCAG" and int(r["Year"]) <= 2025]
rows.sort(key=lambda r: int(r["Year"]))
gcag_json = json.dumps([[int(r["Year"]), float(r["Mean"])] for r in rows],
                       separators=(",", ":"))

exercises = {
    "ex1_waves_template.html": "ex1-waves.html",
    "ex2_rhythm_template.html": "ex2-rhythm.html",
    "ex3_phantom_template.html": "ex3-phantom-cycles.html",
    "ex4_hidden_years_template.html": "ex4-hidden-years.html",
    "ex5_resonance_template.html": "ex5-resonance.html",
}
outdir = ROOT / "exercises"
outdir.mkdir(exist_ok=True)
for src_name, out_name in exercises.items():
    page = (EX / src_name).read_text()
    page = page.replace("{{SHARED_CSS}}", shared_css)
    page = page.replace("{{SHARED_JS}}", shared_js)
    page = page.replace("{{GCAG_JSON}}", gcag_json)
    assert "{{" not in page, f"unreplaced placeholder in {src_name}"
    (outdir / out_name).write_text(page)
    print(f"done: {outdir / out_name}  ({(outdir / out_name).stat().st_size/1e3:.0f} kB)")
