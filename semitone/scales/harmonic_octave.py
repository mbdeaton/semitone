"""HarmonicOctave: a just-tempered scale"""

from fractions import Fraction
from . import Tone, JustTempered


class HarmonicOctave(JustTempered):
    """Harmonic series reduced into the octave above the principle (exclusive).

    For each harmonic 1, 2, 3, ... an octave shift is applied to bring the
    frequency within the octave above the principle. Duplicate tones, for
    example 2, 4, 8, ... (all duplicates of the principle), are removed to
    produce a set of unique primary tones within the octave.
    """

    def __init__(self, key_name: str, max_multiplier: int) -> None:
        super().__init__(key_name)
        self.scale_name = f"{key_name} harm"

        ratios = self._unique_reduced_ratios(max_multiplier)
        self.primaries = tuple(self._ratio_to_tone(r) for r in ratios)

    def _reduced_ratio(self, n: int) -> Fraction:
        """Reduce integer n into the interval [1, 2) by dividing by 2."""
        ratio = Fraction(n)
        while ratio >= 2:
            ratio /= 2
        return ratio

    def _unique_reduced_ratios(self, max_multiplier: int):
        """Return a sorted list of unique reduced ratios for 1..max_multiplier.

        Uses a set to deduplicate ratios (Fraction is hashable) and returns
        them in ascending order.
        """
        ratios = {self._reduced_ratio(n) for n in range(1, max_multiplier + 1)}
        return sorted(ratios)

    def _ratio_to_tone(self, ratio: Fraction) -> Tone:
        """Convert a fractional ratio to a `Tone` relative to the principle."""
        freq = self.freq_from_fraction_of_primary(self.principle.freq, ratio)
        return Tone(freq)
