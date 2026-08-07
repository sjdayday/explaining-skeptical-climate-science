"""
Extract figure images from the L&S11 arXiv preprint (sources/, true PDF) for
the case file's "Working from the source paper to the rebuttal" section.

Each output is a 2x-resolution crop of the preprint page containing the
figure: the union of the page's raster images, any vector drawings, and the
text blocks that belong to the figure (axis tick labels, the "Figure N"
line, and — where present — the printed legend), excluding the bare page
number. Nothing is redrawn; text and labelling are preserved as printed.

Outputs (to ../figures/): ls11_fig1.png ... ls11_fig5.png, ls11_figsup1.png
Dep: pymupdf
"""

import os
import re

import fitz

_here = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(_here, "..")
SRC = os.path.join(ROOT, "sources", "loehlescafetta1206_5845v1.pdf")
OUT = os.path.join(ROOT, "figures")

# preprint PDF page (1-indexed) -> output name
FIGURE_PAGES = {
    31: "ls11_fig1",
    32: "ls11_fig2",
    33: "ls11_fig3",
    34: "ls11_fig4",
    35: "ls11_fig5",
    38: "ls11_figsup1",
}

doc = fitz.open(SRC)

for pageno, name in FIGURE_PAGES.items():
    page = doc[pageno - 1]
    img = fitz.Rect()
    for info in page.get_image_info():
        img |= fitz.Rect(info["bbox"])
    for d in page.get_drawings():
        img |= d["rect"]
    clip = fitz.Rect(img)
    if pageno == 38:
        # SI page: body text above the figure; keep everything from the top
        # of the figure down (tick labels + the full printed legend), except
        # the bare page number.
        for block in page.get_text("blocks"):
            r, text = fitz.Rect(block[:4]), block[4].strip()
            if re.fullmatch(r"\d{1,2}", text):
                continue
            if r.y1 >= img.y0 - 4:
                clip |= r
    else:
        # figure-only page: everything except the bare page number
        probe = fitz.Rect(img.x0 - 20, img.y0 - 14, img.x1 + 20, img.y1 + 14)
        for block in page.get_text("blocks"):
            r, text = fitz.Rect(block[:4]), block[4].strip()
            if re.fullmatch(r"\d{1,2}", text):
                continue
            if r.intersects(probe) or text.startswith("Figure"):
                clip |= r
    clip = fitz.Rect(clip.x0 - 6, clip.y0 - 6, clip.x1 + 6, clip.y1 + 6) & page.rect
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=clip)
    path = os.path.join(OUT, name + ".png")
    pix.save(path)
    print(f"{name}: page {pageno}, {pix.width}x{pix.height}px -> {path}")

print("done")
