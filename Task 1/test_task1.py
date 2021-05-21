"""
Test case to verify task 1
"""
from task1 import fib_value_length


def test_fib_value_length():
    def fibonacci(n):
        """
        Calculates fib
        :param n: provided value
        :return: result
        """
        a, b = 1, 1
        while n > 2:
            a, b, n = b, b + a, n - 1
        return b

    assert fib_value_length()['number'] == fibonacci(fib_value_length()['idx'])


def test_check_digit_len(n: int = 1000):
    assert len(str(fib_value_length()['number'])) > n
