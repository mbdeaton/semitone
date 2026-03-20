"""SpiralPlotStyle"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SpiralPlotStyle:
    """Internal visual style settings for SpiralPlot rendering."""

    marker_symbols: tuple[str, ...] = (
        "circle",
        "star",
        "triangle-down",
    )
    marker_size: int = 12
    marker_opacity: float = 0.5
    marker_line_width: int = 1
    marker_line_color: str = "white"
    width: int = 600
    height: int = 600
    legend_title_text: str = "Scale"
    angular_tick_values: tuple[int, ...] = tuple(range(0, 360, 30))


DEFAULT_SPIRAL_PLOT_STYLE = SpiralPlotStyle()
