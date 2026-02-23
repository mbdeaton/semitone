"""Feature: Generate and manipulate sequences of tones aka scales."""

import unittest
import semitone as st


class TestScale(unittest.TestCase):
    """Feature tests for manipulations and comparisons of Scales."""

    def test_compare_primaries_of_synonymous_scales(self):
        self.assertScalesUseSameNotes(st.Major("C"), st.Minor("A"))
        self.assertScalesUseSameNotes(st.Major("C"), st.DiatonicMode("C", 1))

    def test_extend_scale_by_number_of_octaves(self):
        base_scale = st.Major("C")
        octaves_below = 1
        octaves_above = 1
        extended_scale = base_scale.extend(octaves_below, octaves_above)
        list_of_subscales = self.split_multi_octave_scale(
            extended_scale, len(base_scale.primaries)
        )
        total_octaves = octaves_below + octaves_above + 1
        self.assertEqual(len(list_of_subscales), total_octaves)
        for scale in list_of_subscales:
            self.assertScalesUseSameNotes(base_scale, scale)

    def split_multi_octave_scale(
        self, scale: st.Scale, num_primaries: int
    ) -> list[st.Arbitrary]:
        """Return a list of single-octave Scales from a multi-octave Scale."""
        scales = []
        num_tones = len(scale.primaries)
        if num_tones % num_primaries != 0:
            raise ValueError(
                f"{num_tones} tones is not divisible by {num_primaries}"
            )
        num_octaves = num_tones // num_primaries
        for octave in range(num_octaves):
            start_index = octave * num_primaries
            end_index = start_index + num_primaries
            octave_tones = scale.primaries[start_index:end_index]
            octave_scale = st.Arbitrary(
                tuple(tone.freq for tone in octave_tones)
            )
            scales.append(octave_scale)
        return scales

    def assertScalesUseSameNotes(
        self, scale_1: st.Scale, scale_2: st.Scale
    ) -> None:
        """Assert two Scales are played with the same keys on the keyboard."""
        for t1 in scale_1.primaries:
            if not any(t1.same_pitch_class(t2) for t2 in scale_2.primaries):
                self.fail(f"{t1} not found in Scale {scale_2}")

        for t2 in scale_2.primaries:
            if not any(t2.same_pitch_class(t1) for t1 in scale_1.primaries):
                self.fail(f"{t2} not found in Scale {scale_1}")
