"""
Test case for task 2.
"""
from task3 import zeros_sequence


def test_zeros_sequence():
    assert zeros_sequence(n=168000) == 5
    assert zeros_sequence(n=0) == -1
    assert zeros_sequence(n=-100) == 2
    assert zeros_sequence(n=1) == -1
