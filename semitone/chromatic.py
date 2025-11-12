"""Chromatic: an equal-tempered scale."""

from semitone.tone import Tone
from semitone.equal_tempered import EqualTempered


class Chromatic(EqualTempered):
    """The 12 notes from a piano keyboard."""

    def __init__(self, key_name: str) -> None:
        """Initialize. See args for EqualTempered."""
        super().__init__(key_name)
        self.scale_name = f"{key_name} chrom"
        self.primaries = tuple(
            Tone(self.ith_freq_from_primary(self.principle.freq, i))
            for i in range(12)
        )

    def note_names(self) -> list[str]:
        """Return 12 note names, rising, starting from the key principle"""
        offset = EqualTempered.find_chromatic_index(self.key_name)
        names_from_c = self.note_names_including_enharmonics()
        return names_from_c[offset:] + names_from_c[:offset]
