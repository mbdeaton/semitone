"""Feature: Generate and manipulate sequences of tones aka scales."""

# TODO make it so you only import Scale
from semitone.scale import Scale
from semitone.chromatic import Chromatic
from semitone.major import Major
from semitone.minor import Minor
from semitone.diatonic_mode import DiatonicMode
import unittest


class TestScale(unittest.TestCase):
    """Feature tests for the Scale class."""

    def test_get_principle_and_primaries_as_floats(self):
        scales_and_inits = [
            (Chromatic, "C"),
            (Major, "C"),
        ]
        for scale, init in scales_and_inits:
            with self.subTest(scale=scale, initializer=init):
                s = scale(init)
                self.assertIsInstance(s.principle, float)
                for tone in s.primaries:
                    self.assertIsInstance(tone, float)

    def test_compute_principle_of_equal_tempered_scales_as_expected(self):
        principle = {"name": "C", "freq": 261.63}
        for scale_type in (Chromatic, Major, Minor):
            with self.subTest(scale_type=scale_type):
                s = scale_type(principle["name"])
                self.assertAlmostEqual(s.principle, principle["freq"], places=2)

    def test_compare_primaries_of_synonymous_scales(self):
        self.assertScalesUseSameNotes(Major("C"), Minor("A"))
        self.assertScalesUseSameNotes(Major("C"), DiatonicMode("C", 1))

    def assertScalesUseSameNotes(self, scale_1: Scale, scale_2: Scale) -> None:
        """Assert two Scales are played with the same keys on the keyboard.

        If one scale starts on a lower tone, then it is windowed to the higher
        scale by pitching too-low tones up by one or more octaves. So, for
        example, if scale_1 is C maj and scale_2 is A min, the first two tones
        of A min are shifted up by an octave.
        """
        if scale_1.principle > scale_2.principle:
            scale_1, scale_2 = scale_2, scale_1

        min_tone = min(scale_1.primaries)
        max_tone = max(scale_1.primaries)
        scale_2_primaries = []
        for tone in scale_2.primaries:
            while tone < min_tone:
                tone *= 2
            while tone > max_tone:
                tone /= 2
            scale_2_primaries.append(tone)
        scale_2_primaries = sorted(scale_2_primaries)

        for note_1, note_2 in zip(scale_1.primaries, scale_2_primaries):
            self.assertAlmostEqual(note_1, note_2, places=7)
