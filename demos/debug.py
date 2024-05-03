"""Debug script"""

from semitone.major import Major
from semitone.spiral_plot import SpiralPlot

scale = Major("Bb")
print(scale.primaries)
fig = SpiralPlot.draw(scale)
fig.write_image("test.png")
