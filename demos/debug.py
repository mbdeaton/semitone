"""Debug script"""

from semitone.major import Major
from semitone.spiral_plot import SpiralPlot
from semitone.extender import Extender

# This is intended to be scratch code to be modified for debugging purposes
scale = Major("Bb")
print(scale.primaries)
fig = SpiralPlot.draw([scale])
print(Extender.extend(scale, octaves_below=0, octaves_above=0))
