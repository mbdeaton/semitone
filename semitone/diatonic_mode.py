"""DiatonicMode: an equal-tempered scale."""

from semitone.tone import Tone
from semitone.equal_tempered import EqualTempered


class DiatonicMode(EqualTempered):
    """The seven notes from one of the classical diatonic modes."""

    _MODE_NAMES = (
        "ion",
        "dor",
        "phr",
        "lyd",
        "mix",
        "aeo",
        "loc",
    )

    def __init__(self, key_name: str, mode: int) -> None:
        """Initialize. See args for EqualTempered, plus mode below.

        Args:
            mode (int): the mode from 1-7, where 1 is Ionian, 2 is Dorian, etc
        """
        super().__init__(key_name)

        if mode not in range(1, 7):
            raise ValueError("mode must be an int 1-7, inclusive")

        self.scale_name = f"{key_name} {DiatonicMode._MODE_NAMES[mode-1]}"
        self.primaries = tuple(
            Tone(self.ith_freq_from_primary(self.principle.freq, i))
            for i in self.steps_from_mode(mode)
        )

    @staticmethod
    def steps_from_mode(mode: int) -> tuple[int, ...]:
        """Compute the semitone steps of each note in the numbered mode.

        Args:
            mode (int): the mode to compute, from 1-7

        Returns:
            a 7-element tuple of ints, each the number of half-steps above the
            primary tone in the given mode
        """
        base = (0, 2, 4, 5, 7, 9, 11)
        num_halfsteps = 12
        start_step = base[mode - 1]
        steps = [(note - start_step) % num_halfsteps for note in base]
        return tuple(sorted(steps))
