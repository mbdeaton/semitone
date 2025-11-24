"""Tone: a single note."""


class Tone:
    """A note having a distinct frequency.

    Overrides comparators (e.g. equality, less than, greater than) with fuzzy
    comparison, scaled by DELTA_CENTS, to allow small floating point variation.
    """

    DELTA_CENTS = 0.1  # allowable frequency difference in cents for equality

    def __init__(self, freq: float) -> None:
        self.freq = freq
        self._delta = self.freq * self.DELTA_CENTS / 1200

    def __str__(self) -> str:
        return f"{self.freq:.2f}"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tone):
            return NotImplemented
        return abs(self.freq - other.freq) < self._delta

    def same_pitch_class(self, other: object) -> bool:
        """True if two Tones are any n octaves apart, i.e. same pitch class"""
        if not isinstance(other, Tone):
            return NotImplemented
        freq1, freq2 = self.freq, other.freq
        if self.freq > other.freq:
            freq1, freq2 = other.freq, self.freq
        while freq1 < freq2:
            freq2 /= 2
        return Tone(freq1) == Tone(freq2)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Tone):
            return NotImplemented
        return self.freq < other.freq - self._delta

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Tone):
            return NotImplemented
        return self.freq <= other.freq - self._delta

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Tone):
            return NotImplemented
        return self.freq > other.freq + self._delta

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Tone):
            return NotImplemented
        return self.freq >= other.freq + self._delta
