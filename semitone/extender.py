"""Extender"""

from semitone.tone import Tone
from semitone.scale import Scale


class Extender:
    """Extends the primary tones of a scale to higher or lower octaves."""

    @staticmethod
    def extend(scale: Scale, octaves_below: int, octaves_above: int) -> Scale:
        """Return the scale extended to additional octaves

        Args:
            scale (Scale): the collection of notes to extend
            octaves_below, octaves_above (int): how many octaves to extend
                outside the primary scale
        """
        tones = []
        for octave in range(-octaves_below, octaves_above + 1):
            multiplier = 2**octave
            tones.extend(
                [Tone(multiplier * tone.freq) for tone in scale.primaries]
            )
        new_scale = scale
        new_scale.primaries = tuple(tones)
        return new_scale
