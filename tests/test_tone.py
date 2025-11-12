"""Feature: Compare tones robustly against small floating point variation."""

import unittest
from semitone.tone import Tone


class TestTone(unittest.TestCase):
    """Feature tests for the Tone class."""

    _delta_cents = 0.01  # allowable frequency difference in cents for equality
    _jitter_cents = 1e-10  # extra amount to ensure equality/inequality
    _base_freq = 440.0

    def test_compare_slightly_different_tones_expect_equal(self):
        """Tones differing less than accepted delta should compare equal."""

        delta = (
            self._base_freq * (self._delta_cents - self._jitter_cents) / 1200
        )

        base_tone = Tone(self._base_freq)

        varying_tones = (
            Tone(self._base_freq),
            Tone(self._base_freq - delta),
            Tone(self._base_freq + delta),
        )

        for tone in varying_tones:
            with self.subTest(base_tone=base_tone, tone=tone):
                self.assertEqual(base_tone, tone)

    def test_compare_slightly_different_tones_expect_unequal(self):
        """Tones differing more than accepted delta should compare unequal."""

        delta = (
            self._base_freq * (self._delta_cents + self._jitter_cents) / 1200
        )

        base_tone = Tone(self._base_freq)

        varying_tones = (
            Tone(self._base_freq - delta),
            Tone(self._base_freq + delta),
        )

        for tone in varying_tones:
            with self.subTest(base_tone=base_tone, tone=tone):
                self.assertNotEqual(base_tone, tone)
