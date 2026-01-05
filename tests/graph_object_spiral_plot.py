"""GraphObjectSpiralPlot for tests."""

from typing import Iterable

import pandas
import plotly.graph_objects as go


class GraphObjectSpiralPlot:
    """Represents the visible parts of a SpiralPlot, used for testing."""

    def __init__(self, figure: go.Figure) -> None:
        """Initialize.

        Args:
            figure (graph_objects.Figure): the figure to be represented
        """
        self._figure = figure

    def get_polar_points(self) -> Iterable[pandas.DataFrame]:
        """Return the polar plot points (r, theta) for each figure in the SpiralPlot.

        Returns:
            Iterable of pandas.DataFrames, one for each scale represented in the
            SpiralPlot. The structure of each DataFrame is one row per scale
            tone, having columns:

                wavelength (float) : radial coordinate
                angle      (float) : angular coordinate, in degrees
        """
        dataframes = []
        for trace in self._figure.data:
            assert isinstance(trace, go.Scatterpolar)
            df = pandas.DataFrame(
                {
                    "wavelength": trace.r,
                    "angle": trace.theta,
                }
            )
            dataframes.append(df)
        return dataframes
