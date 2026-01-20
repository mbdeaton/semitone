"""Minor: an equal-tempered scale."""

from . import Tone, EqualTempered


class Minor(EqualTempered):
    """The seven notes from a minor scale."""

    def __init__(self, key_name: str) -> None:
        """Initialize. See args for EqualTempered."""
        super().__init__(key_name)
        self.scale_name = f"{key_name} mi"
        self.primaries = tuple(
            Tone(self.ith_freq_from_primary(self.principle.freq, i))
            for i in (0, 2, 3, 5, 7, 8, 10)
        )
