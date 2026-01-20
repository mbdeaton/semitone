"""Visuals module - graphical representations of scales.

This module provides visualization tools for rendering musical scales as
geometric plots. Users can import directly from this module:
    from semitone.visuals import SpiralPlot, SpiralScale
"""

from .spiral_scale import SpiralScale
from .spiral_plot import SpiralPlot

__all__ = [
    "SpiralScale",
    "SpiralPlot",
]
