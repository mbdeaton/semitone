"""Feature: Compare tones robustly against small floating point variation."""

import unittest
from semitone.tone import Tone


class TestTone(unittest.TestCase):
    """Feature tests for the Tone class."""

    DELTA_CENTS = 0.1  # allowable frequency difference in cents for equality
    JITTER_CENTS = 1e-10  # extra amount to ensure equality/inequality
    BASE_FREQ = 440.0

    def test_compare_slightly_different_tones_expect_equal(self):
        delta = self.BASE_FREQ * (self.DELTA_CENTS - self.JITTER_CENTS) / 1200

        base_tone = Tone(self.BASE_FREQ)

        varying_tones = (
            Tone(self.BASE_FREQ),
            Tone(self.BASE_FREQ - delta),
            Tone(self.BASE_FREQ + delta),
        )

        for tone in varying_tones:
            with self.subTest(base_tone=base_tone, tone=tone):
                self.assertEqual(base_tone, tone)

    def test_compare_slightly_different_tones_expect_unequal(self):
        delta = self.BASE_FREQ * (self.DELTA_CENTS + self.JITTER_CENTS) / 1200

        base_tone = Tone(self.BASE_FREQ)

        varying_tones = (
            Tone(self.BASE_FREQ - delta),
            Tone(self.BASE_FREQ + delta),
        )

        for tone in varying_tones:
            with self.subTest(base_tone=base_tone, tone=tone):
                self.assertNotEqual(base_tone, tone)
