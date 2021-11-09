"""Test the utility functions."""

import pathlib
import unittest

from iter_together.utils import iter_together

HERE = pathlib.Path(__file__).parent


class TestUtils(unittest.TestCase):
    """Test the utilities."""

    def test_my_function(self):
        """Test the :func: iter_together function."""
        path_1 = HERE.joinpath("test1.txt")
        path_2 = HERE.joinpath("test2.txt")
        results = iter_together(path_1, path_2)
        expected = [("hello", "goodbye"), ("hi", "ciao"), ("hiya", "tschüss")]
        self.assertEqual(expected, results)
