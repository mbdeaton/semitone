"""Arbitrary: a scale of any tones."""

from . import Tone, Scale


class Arbitrary(Scale):
    """Tones of arbitrary frequencies."""

    def __init__(self, frequencies: tuple[float, ...]) -> None:
        """Initialize.

        Args:
            frequencies (tuple[float]): the frequencies in Hz,
                will be sorted, with the lowest frequency as the principle
        """
        super().__init__()
        self.principle = Tone(frequencies[0])
        self.key_name = f"{self.principle.freq:.2f} Hz"
        self.scale_name = "arb"
        self.primaries = tuple(Tone(freq) for freq in sorted(frequencies))
