"""Debug script"""

from semitone.major import Major
from semitone.spiral_plot import SpiralPlot

# This is intended to be scratch code to be modified for debugging purposes
scale = Major("Bb")
print(scale)
fig = SpiralPlot.draw((scale,))
print(scale.extend(octaves_below=0, octaves_above=0))
