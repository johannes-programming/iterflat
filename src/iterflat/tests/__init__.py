import unittest

__all__ = ["test"]


def test() -> unittest.TextTestResult:
    "This function runs all the tests."
    loader: unittest.TestLoader
    tests: unittest.TestSuite
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir="iterflat.tests")
    return unittest.TextTestRunner().run(tests)
