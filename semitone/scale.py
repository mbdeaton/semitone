"""Scale: the base of the hierarchy."""

from semitone.tone import Tone


class Scale:
    """A series of tones in a distinct order.

    Typical usage of x = Scale() includes print(x), which displays the
    primary frequencies in Hz.
    """

    _A440 = 440  # reference wrt to int'l standard pitch, A4=440 Hz, aka A440

    def __init__(self) -> None:
        self.key_name: str = ""
        self.scale_name: str = ""
        self.primaries: tuple[Tone, ...] = ()
        self.principle: Tone = Tone(0.0)

    def __str__(self) -> str:
        return " ".join([f"{tone}" for tone in self.primaries])

    def __repr__(self) -> str:
        return str(self)
