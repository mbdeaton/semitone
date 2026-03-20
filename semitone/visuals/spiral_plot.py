"""SpiralPlot"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from .. import Scale, EqualTempered
from . import SpiralScale
from ._spiral_plot_style import SpiralPlotStyle, DEFAULT_SPIRAL_PLOT_STYLE


class SpiralPlot:
    """The graphical depiction of one or more scales as logarithmic spirals."""

    @staticmethod
    def draw(
        scales: tuple[Scale, ...],
        octaves_below: int = 0,
        octaves_above: int = 0,
    ) -> go.Figure:
        """Render one or more scales as a spiral polar plot.

        Args:
            scales (list[Scale]): one or more scales to plot,
                with the primary of the first Scale setting the overall key
            octaves_below, octaves_above (int): how many octaves to extend
                outside each primary scale; defaults = don't extend
        Returns:
            a plotly graph_objects.Figure
        """
        combined_df = SpiralPlot._generate_data_for_all_scales(
            scales, octaves_below, octaves_above
        )
        key = scales[0].key_name

        fig = SpiralPlot._build_base_figure(combined_df)
        SpiralPlot._apply_trace_style(fig, DEFAULT_SPIRAL_PLOT_STYLE)
        SpiralPlot._apply_layout_style(
            fig, combined_df, key, DEFAULT_SPIRAL_PLOT_STYLE
        )
        return fig

    @staticmethod
    def _build_base_figure(combined_df: pd.DataFrame) -> go.Figure:
        """Create the base polar scatter figure from prepared plot data."""
        return px.scatter_polar(
            combined_df,
            r="wavelength",
            theta="angle",
            color="name",
            template="simple_white",
            hover_name="name",
        )

    @staticmethod
    def _apply_trace_style(fig: go.Figure, style: SpiralPlotStyle) -> None:
        """Apply marker-level style settings to each series trace."""
        for i, trace in enumerate(fig.data):
            trace.update(
                marker_symbol=style.marker_symbols[i % len(style.marker_symbols)],
                marker_size=style.marker_size,
                marker_opacity=style.marker_opacity,
                marker_line_width=style.marker_line_width,
                marker_line_color=style.marker_line_color,
            )

    @staticmethod
    def _build_angular_tick_labels(key: str) -> tuple[str, ...]:
        """Return note labels used for angular axis ticks."""
        return EqualTempered(key).note_names_including_enharmonics()

    @staticmethod
    def _apply_layout_style(
        fig: go.Figure,
        combined_df: pd.DataFrame,
        key: str,
        style: SpiralPlotStyle,
    ) -> None:
        """Apply layout and axis styling to the figure."""
        max_wavelength = combined_df["wavelength"].max()
        angular_tick_labels = SpiralPlot._build_angular_tick_labels(key)

        fig.update_layout(
            width=style.width,
            height=style.height,
            template=None,
            legend_title_text=style.legend_title_text,
            polar=dict(
                radialaxis=dict(
                    range=[0, max_wavelength],
                    showticklabels=False,
                    showgrid=False,
                    showline=False,
                    ticks="",
                ),
                angularaxis=dict(
                    tickvals=style.angular_tick_values,
                    ticktext=angular_tick_labels,
                ),
            ),
        )

    @staticmethod
    def _generate_data_for_all_scales(
        scales: tuple[Scale, ...],
        octaves_below: int,
        octaves_above: int,
    ) -> pd.DataFrame:
        """Return combined polar plot data for one or more extended scales.

        Each input Scale is first expanded by the requested number of octaves,
        converted to polar coordinates, and then concatenated into a single
        dataframe suitable for plotting.

        Args:
            scales (list[Scale]): the set of scales to convert
            octaves_below, octaves_above (int): how many octaves to extend
                outside each primary scale; defaults = don't extend

        Returns:
            pandas.DataFrame; see SpiralScale.get_dataframe_copy() for details
        """
        overall_key = scales[0].principle
        frames = []
        for scale in scales:
            extended_scale = scale.extend(octaves_below, octaves_above)
            spiral_scale = SpiralScale(extended_scale, overall_key)
            df = spiral_scale.get_dataframe_copy()
            frames.append(df)

        return pd.concat(frames, ignore_index=True)
