from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import sys
import os

args = sys.argv
filename = args[1]
filename_without_ext = os.path.splitext(os.path.basename(filename))[0]

drawing = svg2rlg(filename)
renderPDF.drawToFile(drawing, filename_without_ext + ".pdf")
