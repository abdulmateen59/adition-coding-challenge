"""
Test case for task 2.
"""
from task2 import jumps


def test_jumps():
    assert jumps(-1, -1, -1) == (0, 0)
    assert jumps(0, 0, -1) == (0, 0)
    assert jumps(1, 1, 0) == (0, 0)
    assert jumps(1, 2, 1) == (1, 2)
    assert jumps(2, 1, 1) == (1, 1)
    assert jumps(10, 85, 30) == (3, 100)
    assert jumps(0, 0, 10) == (0, 0)
