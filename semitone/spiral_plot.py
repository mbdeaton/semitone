"""SpiralPlot"""

import plotly.express as px
from plotly import graph_objects
import pandas as pd
from semitone.scale import Scale
from semitone.equal_tempered import EqualTempered
from semitone.extender import Extender
from semitone.spiral_scale import SpiralScale


class SpiralPlot:
    """The graphical depiction of one or more scales as logarithmic spirals."""

    @staticmethod
    def draw(
        scales: tuple[Scale, ...],
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
        big_df = SpiralPlot._generate_data_for_all_scales(
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
            width=600,
            height=600,
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
    def _generate_data_for_all_scales(
        scales: tuple[Scale, ...],
        octaves_below: int,
        octaves_above: int,
        radial_separation: float = 1.02,
    ) -> pd.DataFrame:
        """Return a combined dataframe of polar plot data for multiple scales.

        Each input Scale is first expanded by the requested number of octaves,
        converted to polar coordinates, and then concatenated into a single
        dataframe suitable for plotting.  A small radial rescaling is applied
        to every scale after the first, so identical tones do not perfectly
        overlap on the plot.

        Args:
            scales (list[Scale]): the set of scales to convert
            octaves_below, octaves_above (int): how many octaves to extend
                outside each primary scale; defaults = don't extend
            radial_separation (float): multiplicative factor applied to the
                radii of each scale after the first; default = 1.01

        Returns:
            For structure of pandas.DataFrame see generate_data_for_one_scale
        """
        overall_key = scales[0].principle
        frames = []
        for i, scale in enumerate(scales):
            extended_scale = Extender.extend(
                scale, octaves_below, octaves_above
            )
            spiral_scale = SpiralScale(extended_scale, overall_key)
            df = spiral_scale.get_dataframe_copy()

            # apply slight radial offset to distinguish overlaps
            if i > 0:
                df["wavelength"] *= radial_separation**i

            frames.append(df)

        return pd.concat(frames, ignore_index=True)
