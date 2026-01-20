"""Debug script"""

import semitone as st

# This is intended to be scratch code to be modified for debugging purposes
scale = st.Major("Bb")
print(scale)
fig = st.SpiralPlot.draw((scale,))
print(scale.extend(octaves_below=0, octaves_above=0))
