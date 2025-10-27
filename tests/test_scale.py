"""Feature: Generate and manipulate sequences of tones aka scales."""

# TODO make it so you only import Scale
from semitone.chromatic import Chromatic
from semitone.major import Major
from semitone.minor import Minor
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
