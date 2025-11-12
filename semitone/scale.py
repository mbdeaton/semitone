"""Scale: the base of the hierarchy."""

from typing import Sequence


class Scale:
    """A series of tones in a distinct order.

    Typical usage of x = Scale() includes print(x), which displays the
    primary frequencies in Hz.
    """

    _A440 = 440  # reference wrt to int'l standard pitch, A4=440 Hz, aka A440

    def __init__(self) -> None:
        self.key_name: str = ""
        self.scale_name: str = ""
        self.primaries: Sequence[float] = ()
        self.principle: float = 0

    def __str__(self) -> str:
        return " ".join([f"{freq:.2f}" for freq in self.primaries])

    def __repr__(self) -> str:
        return str(self)
