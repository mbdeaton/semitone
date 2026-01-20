"""Scales module - musical scale representations and tone definitions.

This module provides the core classes for representing musical scales and tones.
Users can import directly from this module:
    from semitone.scales import Major, Minor, Tone
"""

from .tone import Tone
from .scale import Scale
from .arbitrary import Arbitrary
from .equal_tempered import EqualTempered
from .just_tempered import JustTempered
from .chromatic import Chromatic
from .diatonic_mode import DiatonicMode
from .major import Major
from .minor import Minor

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
]
