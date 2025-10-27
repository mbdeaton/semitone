"""DiatonicMode: an equal-tempered scale."""

from semitone.equal_tempered import EqualTempered


class DiatonicMode(EqualTempered):
    """The seven notes from one of the classical diatonic modes.

    The following modes correspond to the given init arg `mode`:
    1. Ionian (aka Major)
    2. Dorian
    3. Phrygian
    4. Lydian
    5. Mixolydian
    6. Aeolian (aka Minor)
    7. Locrian
    """

    def __init__(self, key_name: str, mode: int) -> None:
        """Initialize. See args for EqualTempered, plus mode below.

        Args:
            mode (int): the mode from 1-7, where 1 is Ionian, 2 is Dorian, etc
        """
        super().__init__(key_name)
        self.primaries = tuple(
            self.ith_freq_from_primary(self.principle, i)
            for i in self.steps_from_mode(mode)
        )

    @staticmethod
    def steps_from_mode(mode: int) -> tuple[int]:
        """Compute the semitone steps of each note in the numbered mode.

        Args:
            mode (int): the mode to compute, from 1-7

        Returns:
            the 7 notes in the mode, represented as half-steps above the primary
        """
        if mode not in range(1, 7):
            raise ValueError("mode must be an int 1-7, inclusive")
        base = (0, 2, 4, 5, 7, 9, 11)
        num_halfsteps = 12
        start_step = base[mode - 1]
        steps = [(note - start_step) % num_halfsteps for note in base]
        return sorted(steps)
