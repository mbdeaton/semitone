"""Feature: Compare tones with robustness against small floating point variation."""

import unittest
import semitone.tone as tone


class TestTone(unittest.TestCase):
    """Feature tests for the Tone class."""

    def test_compare_slightly_different_tones(self):
        """Tones that differ by a tiny amount should compare as equal."""
        base_frequency = 440.0
        delta = 1e-10
        jitter = 1e-16
        base_tone = Tone(frequency=base_frequency)
        tones_expected_same = (
            Tone(frequency=base_frequency),
            Tone(frequency=base_frequency - delta),
            Tone(frequency=base_frequency + delta),
        )
        tones_expected_different = (
            Tone(frequency=base_frequency - delta - jitter),
            Tone(frequency=base_frequency + delta + jitter),
        )

        for tone in tones_expected_same:
            with self.subTest(base_tone=base_tone, tone=tone):
                self.assertEquals(base_tone, tone)

        for tone in tones_expected_different:
            with self.subTest(base_tone=base_tone, tone=tone):
                self.assertNotEquals(base_tone, tone)
