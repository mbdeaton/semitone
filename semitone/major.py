"""Major: an equal-tempered scale."""

from semitone.equal_tempered import EqualTempered


class Major(EqualTempered):
    """The seven notes from a major scale."""

    def __init__(self, key_name: str) -> None:
        """Initialize. See args for EqualTempered."""
        super().__init__(key_name)
        self.scale_name = f"{key_name} ma"
        self.primaries = tuple(
            self.ith_freq_from_primary(self.principle, i)
            for i in (0, 2, 4, 5, 7, 9, 11)
        )
