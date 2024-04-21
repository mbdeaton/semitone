"""Feature: Draw tones on a logarithmic spiral."""

from semitone.chromatic import Chromatic
from semitone.spiral_plot import SpiralPlot
import unittest


class TestDraw(unittest.TestCase):
    """Feature tests for the SpiralPlot class."""

    def test_see_all_tones_as_points_at_expected_radial_positions(self):
        # TODO: silence the figure show (opening a browser tab)
        scale = Chromatic("C")
        points_expected = zip(
            [pow(0.5, i / 12) for i in range(12)],  # r
            [30 * i for i in range(12)],  # theta
        )
        fig = SpiralPlot.draw(scale)  # a tuple of plots
        points_seen = zip(fig.data[0].r, fig.data[0].theta)
        for i, (expected, seen) in enumerate(zip(points_expected, points_seen)):
            self.assertAlmostEqual(
                expected[0], seen[0], places=5, msg=f"Error in {i}th radius"
            )
            # mod 360, to normalize all angles to the range [0,360) deg
            self.assertAlmostEqual(
                expected[1] % 360, seen[1] % 360, places=5, msg=f"Error in {i}th angle"
            )
