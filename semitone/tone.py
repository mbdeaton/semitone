"""Tone: a single note."""


class Tone:
    """A note having a distinct frequency."""

    _delta_cents = 0.01  # allowable frequency difference in cents for equality

    def __init__(self, freq: float) -> None:
        self.freq = freq
        self._delta = self.freq * self._delta_cents / 1200

    def __str__(self) -> str:
        return str(self.freq)

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tone):
            return NotImplemented
        return abs(self.freq - other.freq) < self._delta
