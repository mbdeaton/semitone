"""Feature: Generate and manipulate sequences of tones aka scales."""

# TODO make it so you only import Scale
from semitone.tone import Tone
from semitone.scale import Scale
from semitone.arbitrary import Arbitrary
from semitone.chromatic import Chromatic
from semitone.major import Major
from semitone.minor import Minor
from semitone.diatonic_mode import DiatonicMode
import unittest


class TestScale(unittest.TestCase):
    """Feature tests for the Scale class."""

    def test_compute_principle_frequency_of_equal_tempered_scales(self):
        principle = {"name": "C", "principle tone": Tone(261.626)}
        for scale_type in (Chromatic, Major, Minor):
            with self.subTest(scale_type=scale_type):
                s = scale_type(principle["name"])
                self.assertEqual(s.principle, principle["principle tone"])

    def test_compute_primary_frequencies_of_equal_tempered_scales(self):
        expected_scales = {
            "C maj": Arbitrary(
                (261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88)
            ),
            "C min": Arbitrary(
                (261.63, 293.66, 311.13, 349.23, 392.00, 415.30, 466.16)
            ),
            "C dor": Arbitrary(
                (261.63, 293.66, 311.13, 349.23, 392.00, 440.00, 466.16)
            ),
        }
        scales = (
            ("C maj", Major("C")),
            ("C min", Minor("C")),
            ("C dor", DiatonicMode("C", 2)),
        )
        for scale_name, scale in scales:
            with self.subTest(scale_name=scale_name):
                self.assertEqual(scale, expected_scales[scale_name])

    def test_compare_primaries_of_synonymous_scales(self):
        self.assertScalesUseSameNotes(Major("C"), Minor("A"))
        self.assertScalesUseSameNotes(Major("C"), DiatonicMode("C", 1))

    def assertScalesUseSameNotes(self, scale_1: Scale, scale_2: Scale) -> None:
        """Assert two Scales are played with the same keys on the keyboard."""
        for t1 in scale_1.primaries:
            if not any(t1.same_pitch_class(t2) for t2 in scale_2.primaries):
                self.fail(f"{t1} not found in Scale {scale_2}")

        for t2 in scale_2.primaries:
            if not any(t2.same_pitch_class(t1) for t1 in scale_1.primaries):
                self.fail(f"{t2} not found in Scale {scale_1}")
