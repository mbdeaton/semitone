# Semitone
A Python package to represent tones, scales, and chords geometrically.

Published at [pypi.org/project/semitone](https://pypi.org/project/semitone).

### Quick Start
For full demos, see the notebooks in `demos/`.

Install with pip:
```sh
pip install semitone
```

Analyze scales:
```py
import semitone as st

scale = st.Major("A")

# Compute frequencies
print(scale)
print(scale.extend(octaves_below=0, octaves_above=2))

# Visualize as a logarithmic spiral
fig = st.SpiralPlot.draw((scale,))
fig.show()

# Visualize equal- vs just-tempered scales together
scale_harm = st.HarmonicSeries("A", max_multiplier=13)
fig = st.SpiralPlot.draw((scale, scale_harm))
fig.show()
```

### Contributing
For contributing guidelines, see `CONTRIBUTING.md`.
