"""Feature: Generate and manipulate sequences of tones aka scales."""

# TODO make it so you only import Scale
from semitone.tone import Tone
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
                self.assertIsInstance(s.principle.freq, float)
                for tone in s.primaries:
                    self.assertIsInstance(tone.freq, float)

    def test_compute_principle_of_equal_tempered_scales_as_expected(self):
        principle = {"name": "C", "principle tone": Tone(261.626)}
        for scale_type in (Chromatic, Major, Minor):
            with self.subTest(scale_type=scale_type):
                s = scale_type(principle["name"])
                self.assertEqual(s.principle, principle["principle tone"])

    def test_compare_primaries_of_synonymous_scales(self):
        self.assert_scales_use_same_notes(Major("C"), Minor("A"))
        self.assert_scales_use_same_notes(Major("C"), DiatonicMode("C", 1))

    def assert_scales_use_same_notes(
        self, scale_1: Scale, scale_2: Scale
    ) -> None:
        """Assert two Scales are played with the same keys on the keyboard."""
        for t1 in scale_1.primaries:
            if not any(t1.same_pitch_class(t2) for t2 in scale_2.primaries):
                self.fail(f"{t1} not found in Scale {scale_2}")

        for t2 in scale_2.primaries:
            if not any(t2.same_pitch_class(t1) for t1 in scale_1.primaries):
                self.fail(f"{t2} not found in Scale {scale_1}")
