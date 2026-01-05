"""Feature: Draw tones on a logarithmic spiral."""

import pandas as pd
from semitone.chromatic import Chromatic
from semitone.spiral_plot import SpiralPlot
import unittest
from tests.graph_object_spiral_plot import GraphObjectSpiralPlot
from pandas.testing import assert_frame_equal


class TestDraw(unittest.TestCase):
    """Feature tests for the SpiralPlot class."""

    TEST_TOL = 1e-5
    DEFAULT_PRINCIPLE_RADIUS = 1.0
    DEFAULT_BASE_RESCALING_FACTOR = 1.02

    def test_see_all_tones_as_points_at_polar_positions(
        self,
    ):
        scale = Chromatic("C")
        fig = SpiralPlot.draw((scale,))
        graph_object = GraphObjectSpiralPlot(fig)
        dfs_actual = graph_object.get_polar_points()
        df_expected = self.generate_points_expected_chromatic(
            principle_angle_deg=0.0,
            principle_radius=self.DEFAULT_PRINCIPLE_RADIUS,
            num_tones=12,
        )
        self.assertEqual(len(dfs_actual), 1)
        assert_frame_equal(
            dfs_actual[0],
            df_expected,
            check_exact=False,
            atol=self.TEST_TOL,
            rtol=0,
        )

    def generate_points_expected_chromatic(
        self,
        principle_angle_deg: float,
        principle_radius: float,
        num_tones: int,
        radial_rescaling: float = 1.0,
    ) -> pd.DataFrame:
        """Return expected polar coords for a chromatic scale.

        Args:
            principle_angle_deg (float): angle of the principle tone, degrees
            principle_radius (float): radius of the principle tone
            num_tones (int): number of tones in the chromatic scale
            radial_rescaling (float): multiplicative factor applied to all
                radii of a single scale; built into SpiralPlot when multiple
                scales are present on a single figure; default = 1.0

        Returns:
            pandas.DataFrame containing the polar coordinate tuples
            (radius, angle) for each tone in the chromatic scale.
            Structure is one row per scale tone, having columns:

                wavelength (float) : radial coordinate of the tone
                angle      (float) : angular coordinate of the tone, in degrees
        """
        points = []
        for i in range(num_tones):
            angle = (principle_angle_deg + (i * 30.0)) % 360
            radius = principle_radius * pow(0.5, i / 12) * radial_rescaling
            points.append((radius, angle))
        return pd.DataFrame(points, columns=("wavelength", "angle"))
