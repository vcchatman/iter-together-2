"""Utility functions for :mod:`iter_together`."""

from typing import List, Tuple


def iter_together(path_1: str, path_2: str) -> List[Tuple[str, str]]:
    """Open two files, zip them, and iterate over them together.

    :param path_1: The file path of the left file
    :param path_2: The file path of the right file
    :returns: Pairs of lines from the two files
    """
    with open(path_1) as file_1, open(path_2) as file_2:
        return iter_together_file(file_1, file_2)


def iter_together_file(file_1: str, file_2: str) -> List[Tuple[str, str]]:
    """Zip two iterables of strings together.

    :param file_1: The left iterable
    :param file_2: The right iterable
    :returns: Pairs of lines from the two files
    """
    results = []
    for line_1, line_2 in zip(file_1, file_2):
        results.append((line_1.strip(), line_2.strip()))
    return results
