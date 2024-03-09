"""SpiralPlot"""

import math
from typing import Iterable, Sequence
import plotly.express as px
from plotly import graph_objects
import pandas as pd
from semitone.scale import Scale


class SpiralPlot:
    """The graphical representation of a scale as a logarithmic spiral."""

    _B_ANGLE = math.log(2) / 2 / math.pi  # scale for angle calculations

    @staticmethod
    def draw(scale: Scale) -> graph_objects.Figure:
        """Render the spiral represenation of the scale in a polar plot.

        Args:
            scale (Scale): the Scale from which to build the spiral

        Returns:
            a plotly graph_objects.Figure
        """
        df = pd.DataFrame(
            data=SpiralPlot.polar_coords_from_freqs(
                scale.primaries, scale.principle),
            columns=("freq", "angle"),
        )
        fig = px.scatter_polar(
            df, r="freq", theta="angle", template="simple_white")
        return fig

    @staticmethod
    def polar_coords_from_freqs(
        frequencies: Sequence[float],
        principle: float | None = None,
        scale: float | None = None,
    ) -> Iterable[tuple[float, float]]:
        """Return polar coords of spiral positions from a given set of tones.

        For radii, frequencies are inverted to get wavelengths and then scaled.
        For angles, the principle tone is placed at 12 o'clock (90 deg), and
        rising tones are placed clockwise around the spiral, with a full octave
        above the principle returning to 12 o'clock.

        Args:
            frequencies (sequence(float)): frequencies of the tones to calculate
            principle (float): the home frequency to be plotted at 12
                o'clock; default is first frequency in the sequence of first arg
            scale (float): the radius to rescale the principle wavelength
                default=1

        Returns:
            a list of 2-tuples of floats representing (radius, angle) for each
            of the input frequencies
        """
        if principle is None:
            principle = frequencies[0]
        if scale is None:
            scale = 1
        radii = [SpiralPlot.radius_from_freq(
            f, principle, scale) for f in frequencies]
        angles = [SpiralPlot.angle_from_freq(
            f, principle) for f in frequencies]
        return zip(radii, angles)

    @staticmethod
    def radius_from_freq(frequency: float, principle: float, scale: float) -> float:
        """Convert a frequency to a scaled wavelength.

        Args:
            frequency (float): frequency in Hz
            principle (float): reference frequency in Hz
            scale (float): reference scale forcing principle wavelength==scale

        Returns:
            the computed radius (float)
        """
        return scale * principle / frequency

    @staticmethod
    def angle_from_freq(frequency: float, principle: float) -> float:
        """Convert a frequency to an angle on [0,360).

        Note, increasing the input frequency increases the angle in the
        polar plot, moving the plotted point clockwise.

        Args:
            frequency (float): frequency in Hz
            principle (float): reference frequency so principle angle==0 deg

        Returns:
            the computed angle in degrees (float)
        """
        # compute in standard physics coords: radians, 0 is east, increase CCW
        angle = math.log(principle / frequency) / \
            SpiralPlot._B_ANGLE + math.pi / 2
        if angle < 0 or angle >= 2 * math.pi:
            angle = angle % (2 * math.pi)
        # convert to plotly polar plot coords: degrees, 0 is north, increase CW
        return (math.pi / 2 - angle) * 180 / math.pi
