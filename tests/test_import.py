"""Feature: Import semitone modules for code explorations."""

import unittest
import importlib


class TestImport(unittest.TestCase):
    """Feature tests for importing the semitone package."""

    MODULES = [
        "semitone",
        "semitone.scales",
        "semitone.visuals",
        "semitone.scales.tone",
        "semitone.scales.scale",
        "semitone.scales.arbitrary",
        "semitone.scales.equal_tempered",
        "semitone.scales.chromatic",
        "semitone.scales.diatonic_mode",
        "semitone.scales.major",
        "semitone.scales.minor",
        "semitone.visuals.spiral_scale",
        "semitone.visuals.spiral_plot",
    ]

    # Top-level API
    PACKAGE_EXPORTS = [
        "Tone",
        "Scale",
        "Arbitrary",
        "EqualTempered",
        "Chromatic",
        "DiatonicMode",
        "Major",
        "Minor",
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
