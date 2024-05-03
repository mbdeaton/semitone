"""Extender"""

from typing import Sequence
from semitone.scale import Scale


class Extender:
    """Extends the primary tones of a scale to higher or lower octaves."""

    @staticmethod
    def extend(
        scale: Scale, octaves_below: int, octaves_above: int
    ) -> Sequence[float]:
        """Return the scale extended to additional octaves

        Args:
            scale (Scale): the collection of notes to extend
            octaves_below, octaves_above (int): how many octaves to extend
                outside the primary scale
        """
        tones = []
        for octave in range(-octaves_below, octaves_above + 1):
            multiplier = 2**octave
            tones.extend([multiplier * tone for tone in scale.primaries])
        return tones
