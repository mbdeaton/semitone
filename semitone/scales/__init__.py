"""Scales module - musical scale representations and tone definitions.

This module provides the core classes for representing musical scales and tones.
Users can import directly from this module:
    from semitone.scales import Major, Minor, Tone
"""

from semitone.scales.tone import Tone
from semitone.scales.scale import Scale
from semitone.scales.arbitrary import Arbitrary
from semitone.scales.equal_tempered import EqualTempered
from semitone.scales.chromatic import Chromatic
from semitone.scales.diatonic_mode import DiatonicMode
from semitone.scales.major import Major
from semitone.scales.minor import Minor

__all__ = [
    "Tone",
    "Scale",
    "Arbitrary",
    "EqualTempered",
    "Chromatic",
    "DiatonicMode",
    "Major",
    "Minor",
]
