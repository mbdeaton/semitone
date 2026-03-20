# Semitone
A Python package for learning and exploration: compute frequencies, scales, and
chords in different tuning systems, and represent their relationships through
geometry.

Semitone is built to help people build intuition for musical relationships
through the physics of sound. It is not intended to be a full music-production
toolkit.

Published at [pypi.org/project/semitone](https://pypi.org/project/semitone).


### Purpose
Use Semitone to explore and compare how tuning systems shape intervals,
harmonies, and scales. The focus is understanding: seeing what is similar,
what is different, and why.


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
with wavelength: higher tones are closer to the center. Angle scales with
the octave distance from key center: semitone increases in pitch correspond to
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
Please keep contributions aligned with Semitone's core purpose: learning and
exploration through clear, physically grounded representations of music.
