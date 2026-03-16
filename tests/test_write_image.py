"""Feature: Export plots to various image formats."""

import unittest
import semitone as st
import os


class TestWriteImage(unittest.TestCase):
    """Feature tests for the write_image method in SpiralPlot."""

    def test_write_image_to_file(self):
        """Test that writing an image file works without error."""
        scale = st.Major("A")
        fig = st.SpiralPlot.draw((scale,))

        # Specify the output file path
        output_file = "test_image.png"

        # Attempt to write the image
        try:
            fig.write_image(output_file)
        except (OSError, IOError) as e:
            self.fail(f"Image writing failed with error: {str(e)}")

        # Check if the file was created
        self.assertTrue(
            os.path.isfile(output_file), "Image file was not created."
        )

        # Clean up the created image file
        if os.path.isfile(output_file):
            os.remove(output_file)
