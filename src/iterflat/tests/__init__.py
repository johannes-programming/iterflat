from __future__ import annotations

__all__: list[str] = ["test"]

import unittest


def test() -> unittest.TextTestResult:
    "This function runs all the tests."
    loader: unittest.TestLoader
    suite: unittest.TestSuite
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="iterflat.tests")
    return unittest.TextTestRunner().run(suite)
