"""Feature: Generate a scale's primary frequencies."""

import unittest
import semitone as st


class TestFreqs(unittest.TestCase):
    """Feature tests for specific frequencies present in a Scale."""

    def test_compute_principle_frequency_of_scale(self):
        expected_freq = 261.626
        scale_inits = (
            (st.Arbitrary, ((expected_freq,),)),
            (st.Chromatic, ("C",)),
            (st.Major, ("C",)),
            (st.Minor, ("C",)),
            (st.DiatonicMode, ("C", 2)),
            (st.HarmonicOctave, ("C", 5)),
            (st.HarmonicSeries, ("C", 5)),
        )
        for scale_type, args in scale_inits:
            with self.subTest(scale_type=scale_type):
                s = scale_type(*args)  # type: ignore
                self.assertEqual(s.principle, st.Tone(expected_freq))

    def test_compute_primary_frequencies_of_scale(self):
        expected_scales = {
            "C chrom": st.Arbitrary(
                (261.63, 277.18, 293.66, 311.13, 329.63, 349.23)
                + (369.99, 392.00, 415.30, 440.00, 466.16, 493.88)
            ),
            "C maj": st.Arbitrary(
                (261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88)
            ),
            "C min": st.Arbitrary(
                (261.63, 293.66, 311.13, 349.23, 392.00, 415.30, 466.16)
            ),
            "C dor": st.Arbitrary(
                (261.63, 293.66, 311.13, 349.23, 392.00, 440.00, 466.16)
            ),
            "C harm ser": st.Arbitrary(
                (261.63, 523.25, 784.88, 1046.50, 1308.13, 1569.75, 1831.38)
            ),
            "C harm": st.Arbitrary(
                (261.63, 294.33, 327.03, 359.74, 392.44, 425.14, 457.84)
            ),
        }
        scales = (
            ("C chrom", st.Chromatic("C")),
            ("C maj", st.Major("C")),
            ("C min", st.Minor("C")),
            ("C dor", st.DiatonicMode("C", 2)),
            ("C harm ser", st.HarmonicSeries("C", 7)),
            ("C harm", st.HarmonicOctave("C", 13)),
        )
        for scale_name, scale in scales:
            with self.subTest(scale_name=scale_name):
                self.assertEqual(scale, expected_scales[scale_name])
