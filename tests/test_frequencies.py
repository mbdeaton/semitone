"""Feature: Generate a scale's primary frequencies."""

import unittest
import semitone as st


class TestFreqs(unittest.TestCase):
    """Feature tests for specific frequencies present in a Scale."""

    def test_compute_principle_frequency_of_scale(self):
        expected_freq = 261.626
        scale_inits = (
            (st.Arbitrary, (expected_freq,)),
            (st.Chromatic, ("C",)),
            (st.Major, ("C",)),
            (st.Minor, ("C",)),
            (st.DiatonicMode, ("C", 2)),
            (st.HarmonicOctave, ("C", 10)),
        )
        for scale_type, args in scale_inits:
            with self.subTest(scale_type=scale_type):
                s = scale_type(*args)
                self.assertEqual(s.principle, expected_freq)

    def test_compute_primary_frequencies_of_equal_tempered_scales(self):
        expected_scales = {
            "C maj": st.Arbitrary(
                (261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88)
            ),
            "C min": st.Arbitrary(
                (261.63, 293.66, 311.13, 349.23, 392.00, 415.30, 466.16)
            ),
            "C dor": st.Arbitrary(
                (261.63, 293.66, 311.13, 349.23, 392.00, 440.00, 466.16)
            ),
        }
        scales = (
            ("C maj", st.Major("C")),
            ("C min", st.Minor("C")),
            ("C dor", st.DiatonicMode("C", 2)),
        )
        for scale_name, scale in scales:
            with self.subTest(scale_name=scale_name):
                self.assertEqual(scale, expected_scales[scale_name])
