"""Visuals module - graphical representations of scales.

This module provides visualization tools for rendering musical scales as
geometric plots. Users can import directly from this module:
    from semitone.visuals import SpiralPlot, SpiralScale
"""

from semitone.visuals.spiral_plot import SpiralPlot
from semitone.visuals.spiral_scale import SpiralScale

__all__ = [
    "SpiralPlot",
    "SpiralScale",
]
