"""JustTempered: a scale of perfect ratios."""

from fractions import Fraction
from . import Tone, Scale, EqualTempered


class JustTempered(Scale):
    """Tones from the just temperament tuning system.

    The frequencies are all perfect ratios of a single base frequency.
    """

    def __init__(self, key_name: str) -> None:
        """Initialize

        Args:
            key_name (str): the name of the principle or home note of
                the scale; allowed values are any traditional western keys,
                expressed as 1 or 2 ASCII characters; e.g. Ab, A, A#, etc.
        """
        super().__init__()
        self.key_name = key_name
        self.principle = Tone(EqualTempered.freq_from_name(self.key_name))

    def _tone_from_freq_ratio(self, ratio: Fraction) -> Tone:
        """Compute the Tone given a perfect ratio of the key center's freq.

        Args:
            ratio (Fraction): the perfect ratio of the key center to compute
                the frequency of, e.g. Fraction(3, 2) for a perfect fifth;
                a fraction less than 1 means lower tone than the key center

        Returns:
            the Tone with the computed frequency
        """
        return Tone(self.principle.freq * float(ratio))
