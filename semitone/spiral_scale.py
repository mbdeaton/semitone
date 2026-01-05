"""SpiralScale"""

import math
from typing import Iterable
import pandas as pd
from semitone.tone import Tone
from semitone.scale import Scale


class SpiralScale:
    """The geometric representation of a single scale as a log spiral."""

    _B_ANGLE = math.log(2) / 2 / math.pi  # scale for angle calculations

    def __init__(
        self,
        scale: Scale,
        zeroth_tone: Tone | None = None,
        scaling_factor: float = 1,
    ) -> None:
        """Initialize.

        Args:
            scale (Scale): the scale to be represented as a log spiral
            zeroth_tone (Tone): the Tone to be placed at 12 o'clock position;
                default is the principle Tone of the scale
            scaling_factor (float): the radius to scale the zeroth Tone's
                wavelength to; default=1
        """
        zeroth = scale.principle if zeroth_tone is None else zeroth_tone
        self._dataframe = self._generate_radii_and_angles(
            scale, zeroth, scaling_factor
        )

    def get_dataframe_copy(self) -> pd.DataFrame:
        """Return a copy of the internal dataframe of polar plot data.

        Returns:
            pandas.DataFrame with one row per scale tone, having columns:

                wavelength (float) : radial coordinate of the tone
                angle      (float) : angular coordinate of the tone, in degrees
                name       (str)   : the key name of the Scale
        """
        return self._dataframe.copy()

    def _generate_radii_and_angles(
        self,
        scale: Scale,
        zeroth: Tone,
        scaling_factor: float,
    ) -> pd.DataFrame:
        """Return a dataframe of polar-plot data for a scale.

        Args:
            scale (Scale): the scale from which to build the dataframe
            zeroth (Tone): the Tone to be placed at 12 o'clock position
            scaling_factor (float): the radius to scale the zeroth tone's
                wavelength to

        Returns:
            pandas.DataFrame; see get_dataframe_copy() for details
        """
        coords = self._generate_polar_coords(
            scale.primaries, zeroth, scaling_factor
        )
        df = pd.DataFrame(coords, columns=("wavelength", "angle"))
        df["name"] = scale.scale_name
        return df

    def _generate_polar_coords(
        self,
        tones: tuple[Tone, ...],
        zeroth: Tone,
        scaling_factor: float,
    ) -> Iterable[tuple[float, float]]:
        """Return polar coords of spiral positions from a given set of Tones.

        For radii, frequencies are inverted to get wavelengths and then scaled.
        For angles, the zeroth Tone is placed at 12 o'clock (90 deg), and
        rising tones are placed clockwise around the spiral, with a full octave
        above the zeroth Tone returning to 12 o'clock.

        Args:
            frequencies (sequence(Tone)): series of Tones to calculate
            zeroth (Tone): the home Tone to be plotted at 12 o'clock
            scale (float): the radius to rescale the zeroth wavelength

        Returns:
            a list of 2-tuples of floats representing (radius, angle) for each
            of the input Tones' frequencies
        """
        radii = [
            self._radius_from_freq(t.freq, zeroth.freq, scaling_factor)
            for t in tones
        ]
        angles = [self._angle_from_freq(t.freq, zeroth.freq) for t in tones]
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
    def _angle_from_freq(frequency: float, zeroth: float) -> float:
        """Convert a frequency to an angle on [0,360).

        Note, increasing the input frequency increases the angle in the
        polar plot, moving the plotted point clockwise.

        Args:
            frequency (float): frequency in Hz
            zeroth (float): reference frequency so zeroth angle==0 deg

        Returns:
            the computed angle in degrees (float)
        """
        # compute in standard physics coords: radians, 0 is east, increase CCW
        angle = (
            math.log(zeroth / frequency) / SpiralScale._B_ANGLE + math.pi / 2
        )
        if angle < 0 or angle >= 2 * math.pi:
            angle = angle % (2 * math.pi)
        # convert to plotly polar plot coords: degrees, 0 is north, increase CW
        return (math.pi / 2 - angle) * 180 / math.pi
