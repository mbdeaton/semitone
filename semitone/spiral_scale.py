"""SpiralScale"""

import math
from typing import Iterable
import pandas as pd
from semitone.tone import Tone
from semitone.scale import Scale


class SpiralScale:
    """The geometric representation of a scale as a logarithmic spiral."""

    _B_ANGLE = math.log(2) / 2 / math.pi  # scale for angle calculations

    def __init__(self, scale: Scale, scaling_factor: float = 1) -> None:
        """Initialize.

        Args:
            scale (Scale): the scale to be represented as a log spiral
        """
        self._scaling_factor = scaling_factor
        self._principle_radius = self._radius_from_freq(
            scale.principle.freq, scale.principle.freq, scaling_factor
        )
        self._zeroth_radius = self._principle_radius
        self._dataframe = self._generate_radii_and_angles_from_scale(scale)

    def get_dataframe_copy(self) -> pd.DataFrame:
        """Return a copy of the internal dataframe of polar plot data.

        Returns:
            pandas.DataFrame with one row per scale tone, having columns:

                wavelength (float) : radial coordinate of the tone
                angle      (float) : angular coordinate of the tone, in degrees
                name       (str)   : the key name of the Scale
        """
        return self._dataframe.copy()

    def _generate_radii_and_angles_from_scale(
        self,
        scale: Scale,
    ) -> pd.DataFrame:
        """Return a dataframe of polar-plot data for a scale.

        Args:
            scale (Scale): the scale from which to build the dataframe

        Returns:
            pandas.DataFrame with one row per scale tone, having columns:

                wavelength (float) : radial coordinate of the tone
                angle      (float) : angular coordinate of the tone, in degrees
                name       (str)   : the key name of the Scale
        """
        coords = self._polar_coords_from_freqs(scale.primaries, scale.principle)
        df = pd.DataFrame(coords, columns=("wavelength", "angle"))
        df["name"] = scale.scale_name
        return df

    def _polar_coords_from_freqs(
        self,
        tones: tuple[Tone, ...],
        principle: Tone | None = None,
        scaling_factor: float | None = None,
    ) -> Iterable[tuple[float, float]]:
        """Return polar coords of spiral positions from a given set of tones.

        For radii, frequencies are inverted to get wavelengths and then scaled.
        For angles, the principle tone is placed at 12 o'clock (90 deg), and
        rising tones are placed clockwise around the spiral, with a full octave
        above the principle returning to 12 o'clock.

        Args:
            frequencies (sequence(Tone)): frequencies of the tones to calculate
            principle (Tone): the home frequency to be plotted at 12
                o'clock; default is first frequency in the sequence of first arg
            scale (float): the radius to rescale the principle wavelength
                default=1

        Returns:
            a list of 2-tuples of floats representing (radius, angle) for each
            of the input frequencies
        """
        if principle is None:
            principle = tones[0]
        if scaling_factor is None:
            scaling_factor = 1
        radii = [
            self._radius_from_freq(t.freq, principle.freq, scaling_factor)
            for t in tones
        ]
        angles = [self._angle_from_freq(t.freq, principle.freq) for t in tones]
        return zip(radii, angles)

    @staticmethod
    def _radius_from_freq(
        frequency: float, principle: float, scaling_factor: float
    ) -> float:
        """Convert a frequency to a scaled wavelength.

        Args:
            frequency (float): frequency in Hz
            principle (float): reference frequency in Hz
            scale (float): reference scale forcing principle wavelength==scale

        Returns:
            the computed radius (float)
        """
        return scaling_factor * principle / frequency

    @staticmethod
    def _angle_from_freq(frequency: float, principle: float) -> float:
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
            math.log(principle / frequency) / SpiralScale._B_ANGLE + math.pi / 2
        )
        if angle < 0 or angle >= 2 * math.pi:
            angle = angle % (2 * math.pi)
        # convert to plotly polar plot coords: degrees, 0 is north, increase CW
        return (math.pi / 2 - angle) * 180 / math.pi
