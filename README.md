# Semitone
A Python package to represent tones, scales, and chords geometrically.

Published at [pypi.org/project/semitone](https://pypi.org/project/semitone).


### What is a logarithmic spiral?
Each tone is represented as a point on a logarithmic spiral, with its radius
scaling with wavelength (higher tones closer to the center), and its angle
scaling with its progress around the full octave (semitone raises in pitch are
30 deg clockwise rotations).

For example, three octaves of the chromatic scale in C:
<p>
  <img src="img/chrom_c.png" alt="log spiral for chromatic C scale" width="300" />
</p>


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
