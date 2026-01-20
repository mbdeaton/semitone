"""Feature: Import semitone modules for code explorations."""

import unittest
import importlib


class TestImport(unittest.TestCase):
    """Feature tests for importing the semitone package."""

    MODULES = [
        "semitone",
        "semitone.scales",
        "semitone.visuals",
        "semitone.scales.arbitrary",
        "semitone.scales.chromatic",
        "semitone.scales.diatonic_mode",
        "semitone.scales.equal_tempered",
        "semitone.scales.major",
        "semitone.scales.minor",
        "semitone.scales.scale",
        "semitone.scales.tone",
        "semitone.visuals.spiral_plot",
        "semitone.visuals.spiral_scale",
    ]

    PACKAGE_EXPORTS = [
        "Tone",
        "Scale",
        "Arbitrary",
        "EqualTempered",
        "Chromatic",
        "DiatonicMode",
        "Major",
        "Minor",
        "SpiralScale",
        "SpiralPlot",
    ]

    def test_import_modules(self):
        for name in self.MODULES:
            with self.subTest(module=name):
                mod = importlib.import_module(name)
                # sanity check: importlib returned a module object
                self.assertIsNotNone(mod)

    def test_package_exports(self):
        pkg = importlib.import_module("semitone")
        for name in self.PACKAGE_EXPORTS:
            with self.subTest(export=name):
                self.assertTrue(
                    hasattr(pkg, name), f"semitone.{name} not exported"
                )
