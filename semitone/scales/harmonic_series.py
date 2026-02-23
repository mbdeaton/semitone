"""HarmonicSeries: a just-tempered scale"""

from fractions import Fraction
from . import JustTempered


class HarmonicSeries(JustTempered):
    """The harmonic scale built by multiplying a frequency by 2, 3, 4, ...

    Note, this scale spans multiple octaves.
    """

    def __init__(self, key_name: str, max_multiplier: int) -> None:
        """Initialize. See args for JustTempered, plus max below.

        Args:
            max_multiplier (int): the maximum multiplier of the harmonic series
                to include in the scale; e.g. 12 includes all harmonics from
                1 to 12
        """
        super().__init__(key_name)
        self.scale_name = f"{key_name} harm ser"
        ratios = self._harmonic_ratios(max_multiplier)
        self.primaries = tuple(self._tone_from_freq_ratio(r) for r in ratios)

    def _harmonic_ratios(self, max_multiplier: int):
        """Return a list of the harmonic ratios for 1..max_multiplier."""
        return [Fraction(n) for n in range(1, max_multiplier + 1)]
