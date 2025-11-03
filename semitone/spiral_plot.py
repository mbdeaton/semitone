"""SpiralPlot"""

import math
from typing import Iterable, Sequence
import plotly.express as px
from plotly import graph_objects
import pandas as pd
from semitone.scale import Scale
from semitone.equal_tempered import EqualTempered
from semitone.extender import Extender


class SpiralPlot:
    """The graphical depiction of one or more scales as logarithmic spirals."""

    _B_ANGLE = math.log(2) / 2 / math.pi  # scale for angle calculations

    @staticmethod
    def draw(
        scales: list[Scale],
        octaves_below: int = 0,
        octaves_above: int = 0,
    ) -> graph_objects.Figure:
        """Render the spiral representation of scale(s) in a polar plot.

        Args:
            scales (list[Scale]): one or more scales to plot,
                with the primary of the first Scale setting the overall key
            octaves_below, octaves_above (int): how many octaves to extend
                outside each primary scale; defaults = don't extend
        Returns:
            a plotly graph_objects.Figure
        """
        big_df = SpiralPlot.generate_data_for_all_scales(
            scales, octaves_below, octaves_above
        )

        fig = px.scatter_polar(
            big_df,
            r="wavelength",
            theta="angle",
            color="name",
            template="simple_white",
            hover_name="name",
        )

        key = scales[0].key_name
        max_rad = big_df["wavelength"].max()
        fig.update_layout(
            template=None,
            legend_title_text="Scale",
            polar=dict(
                radialaxis=dict(
                    range=[0, max_rad],
                    showticklabels=False,
                    showgrid=False,
                    ticks="",
                ),
                angularaxis=dict(
                    tickvals=tuple(range(0, 360, 30)),
                    ticktext=EqualTempered(
                        key
                    ).note_names_including_enharmonics(),
                ),
            ),
        )
        return fig

    @staticmethod
    def generate_data_for_all_scales(
        scales: list[Scale],
        octaves_below: int,
        octaves_above: int,
    ) -> pd.DataFrame:
        """Return a combined dataframe of polar plot data for multiple scales.

        Each input Scale is first expanded by the requested number of octaves,
        converted to polar coordinates, and then concatenated into a single
        dataframe suitable for plotting.

        Args:
            scales (list[Scale]): the set of scales to convert
            octaves_below, octaves_above (int): how many octaves to extend
                outside each primary scale; defaults = don't extend

        Returns:
            For structure of pandas.DataFrame see generate_dataframes
        """
        frames = []
        for scale in scales:
            frames.append(
                SpiralPlot.generate_data_for_one_scale(
                    scale, octaves_below, octaves_above
                )
            )
        return pd.concat(frames, ignore_index=True)

    @staticmethod
    def generate_data_for_one_scale(
        scale: Scale,
        octaves_below: int,
        octaves_above: int,
    ) -> pd.DataFrame:
        """Return a dataframe of polar-plot data for a single scale.

        The scale is extended above and/or below its primary octave, the
        resulting frequencies are converted to polar coordinates, and the data
        are returned in tabular form.

        Args:
            scale (Scale): the scale from which to build the dataframe
            octaves_below, octaves_above (int): how many octaves to extend
                outside the primary scale; defaults = don't extend

        Returns:
            pandas.DataFrame with one row per tone in the (possibly extended)
            scale, having the following columns:

                wavelength (float) : radial coordinate of the tone
                angle      (float) : angular coordinate of the tone, in degrees
                name       (str)   : the key name of the Scale
        """
        freqs = Extender.extend(scale, octaves_below, octaves_above)
        coords = SpiralPlot.polar_coords_from_freqs(freqs, scale.principle)
        df = pd.DataFrame(coords, columns=("wavelength", "angle"))
        df["name"] = scale.scale_name
        return df

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
        radii = [
            SpiralPlot.radius_from_freq(f, principle, scale)
            for f in frequencies
        ]
        angles = [SpiralPlot.angle_from_freq(f, principle) for f in frequencies]
        return zip(radii, angles)

    @staticmethod
    def radius_from_freq(
        frequency: float, principle: float, scale: float
    ) -> float:
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
        angle = (
            math.log(principle / frequency) / SpiralPlot._B_ANGLE + math.pi / 2
        )
        if angle < 0 or angle >= 2 * math.pi:
            angle = angle % (2 * math.pi)
        # convert to plotly polar plot coords: degrees, 0 is north, increase CW
        return (math.pi / 2 - angle) * 180 / math.pi
