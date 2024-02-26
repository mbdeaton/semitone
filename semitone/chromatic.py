"""Chromatic: an equal-tempered scale."""

from semitone.equal_tempered import EqualTempered


class Chromatic(EqualTempered):
    """The 12 notes from a piano keyboard."""

    def __init__(self, key_name: str) -> None:
        """Initialize. See args for EqualTempered."""
        super().__init__(key_name)
        self.primaries = tuple(
            self.ith_freq_from_primary(self.principle, i) for i in range(12)
        )
