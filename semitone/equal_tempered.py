"""EqualTempered: a scale on a grid."""

from semitone.scale import Scale


class EqualTempered(Scale):
    """Tones from the traditional tuning of a piano.

    The frequencies live on a grid equally-spaced in log frequency,
    with 12 pitches (aka semitones) between each octave. The grid is
    referenced to international standard pitch, A4=440 Hz.
    """

    _SPELLINGS = (
        ("C",),
        ("Db", "C#"),
        ("D",),
        ("Eb", "D#"),
        ("E",),
        ("F",),
        ("Gb", "F#"),
        ("G",),
        ("Ab", "G#"),
        ("A",),
        ("Bb", "A#"),
        ("B",),
    )

    def __init__(self, key_name: str) -> None:
        """Initialize

        Args:
            key_name (str): the name of the principle or home note of
                the scale; allowed values are any traditional western keys,
                expressed as 1 or 2 ASCII characters; e.g. Ab, A, A#, etc.
        """
        super().__init__()
        self.key_name = key_name
        self.principle = self.freq_from_name(self.key_name)

    @staticmethod
    def ith_freq_from_primary(key_center: float, i: int) -> float:
        """Compute the frequency i semitones above the given key center.

        The tuning is equal-tempered yielding 12 semitones to an octave.

        Args:
            key_center (float): the frequency of the home tone in Hz
            i (int): number of half-steps above key_center,
                indexed from 0, negative i means step down

        Returns:
            the computed frequency (float)
        """
        return key_center * pow(2, i / 12)

    @staticmethod
    def freq_from_name(name: str, octave: int = 4) -> float:
        """Lookup the frequency associated with a traditional western note name.

        Args:
            name (str): the name of the note,
                expressed as 1 or 2 ASCII characters; e.g. Ab, A, A#, etc.
            octave (int): the octave to draw from in scientific pitch notation;
                for example the 4th octave beginning at Middle C covers
                approximately 262-523 Hz; default=4
        """
        for i, enharmonics in enumerate(EqualTempered._SPELLINGS):
            if name in enharmonics:
                index = i
                break
        else:
            raise ValueError(f"Name {name} is not an equal-tempered note name")
        freq_c4 = EqualTempered.ith_freq_from_primary(Scale._A440, -9)
        frequencies = tuple(
            EqualTempered.ith_freq_from_primary(freq_c4, i) for i in range(12)
        )
        return frequencies[index] * 2 ** (octave - 4)
