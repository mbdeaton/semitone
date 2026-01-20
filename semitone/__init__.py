"""Semitone - geometric representations of tones, scales, and chords.

This package provides classes to represent and visualize musical scales,
tones, and chords geometrically.

Quick start:
    >>> from semitone import Major, SpiralPlot
    >>> scale = Major("C")
    >>> print(scale)
    >>> fig = SpiralPlot.draw((scale,))
    >>> fig.show()

Main classes:
    Tone: A single note with a distinct frequency
    Scale: A series of tones in a distinct order
    Major, Minor, Chromatic: Specific scale types
    SpiralPlot: Graphical representation of scales as spiral plots
"""

from semitone.scales.tone import Tone
from semitone.scales.scale import Scale
from semitone.scales.arbitrary import Arbitrary
from semitone.scales.equal_tempered import EqualTempered
from semitone.scales.chromatic import Chromatic
from semitone.scales.diatonic_mode import DiatonicMode
from semitone.scales.major import Major
from semitone.scales.minor import Minor
from semitone.visuals.spiral_scale import SpiralScale
from semitone.visuals.spiral_plot import SpiralPlot

__all__ = [
    "Tone",
    "Scale",
    "Arbitrary",
    "EqualTempered",
    "Chromatic",
    "DiatonicMode",
    "Major",
    "Minor",
    "SpiralScale",
    "SpiralPlot",
]
