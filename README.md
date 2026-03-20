# Semitone
A Python package to compute frequencies, scales, and chords in different tuning
systems, and to represent their relationships through geometry.

Published at [pypi.org/project/semitone](https://pypi.org/project/semitone).


### Quick Start
For full demos, see the notebooks in `demos/`.

Install with pip:
```bash
pip install semitone
```

Analyze scales:
```python
import semitone as st

scale = st.Major("C")

# Compute frequencies
print(scale)
print(scale.extend(octaves_below=0, octaves_above=2))

# Visualize as a logarithmic spiral
fig = st.SpiralPlot.draw((scale,))
fig.show()

# Visualize equal- vs just-tempered scales together
scale_harm = st.HarmonicOctave("C", max_multiplier=19)
fig = st.SpiralPlot.draw((scale, scale_harm))
fig.show()
```


### Music and Geometry
Each tone may be represented as a point on a logarithmic spiral. Radius scales
with wavelength: higher tones are closer to the center. And angle scales with
the octave disance from key center: semitone increases in pitch correspond to
30 deg clockwise rotations.

For example, three octaves of the equal-tempered chromatic scale in C:

![log spiral chromatic C](https://raw.githubusercontent.com/mbdeaton/semitone/refs/heads/main/img/chrom_c.png)

And a just-tempered scale using the first 23 harmonics compressed to a single
octave in C (redundant tones of the same pitch class are eliminated):

![log spiral harmonic-23 C](https://raw.githubusercontent.com/mbdeaton/semitone/refs/heads/main/img/harm_c.png)

And an overlay of the C major scale with the D minor scale:

![log spiral major C and minor D](https://raw.githubusercontent.com/mbdeaton/semitone/refs/heads/main/img/maj_c_min_d.png)


### Contributing
For contributing guidelines, see `CONTRIBUTING.md`.
