"""Semitone - geometric representations of tones, scales, and chords.

This package provides classes to represent and visualize musical scales,
tones, and chords geometrically.

Quick start:
    >>> import semitone as st
    >>> scale = st.Major("C")
    >>> print(scale)
    >>> fig = st.SpiralPlot.draw((scale,))
    >>> fig.show()

Main classes:
    Tone: A single note with a distinct frequency
    Scale: A series of tones in a distinct order
    Major, Minor, Chromatic, ...: Specific scale types
    SpiralPlot: Graphical representation of scales as spiral plots
"""

from .scales.tone import Tone
from .scales.scale import Scale
from .scales.arbitrary import Arbitrary
from .scales.equal_tempered import EqualTempered
from .scales.just_tempered import JustTempered
from .scales.chromatic import Chromatic
from .scales.diatonic_mode import DiatonicMode
from .scales.major import Major
from .scales.minor import Minor
from .visuals.spiral_plot import SpiralPlot

__all__ = [
    "Tone",
    "Scale",
    "Arbitrary",
    "EqualTempered",
    "JustTempered",
    "Chromatic",
    "DiatonicMode",
    "Major",
    "Minor",
    "SpiralPlot",
]
