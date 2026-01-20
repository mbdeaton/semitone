"""HarmonicSeries: a just-tempered scale"""

from fractions import Fraction
from . import Tone, JustTempered


class HarmonicSeries(JustTempered):
    """The harmonic scale built by multiplying a frequency by 2, 3, 4, ..."""

    def __init__(self, key_name: str, max_multiplier: int) -> None:
        """Initialize. See args for JustTempered, plus max below.
        Args:
            max_multiplier (int): the maximum multiplier of the harmonic series
                to include in the scale; e.g. 12 includes all harmonics from
                1 to 12
        """
        super().__init__(key_name)
        self.scale_name = f"{key_name} harm"
        self.primaries = tuple(
            Tone(
                self.freq_from_fraction_of_primary(
                    self.principle.freq, Fraction(n)
                )
            )
            for n in range(1, max_multiplier + 1)
        )
