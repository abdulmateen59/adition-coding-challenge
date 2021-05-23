"""
Write an efficient function that returns the index i for the first Fibonacci number that has more than 1000 digits i.e.
F(i) has 1000 or more decimal digits and F(i-1) has less than 1000 digits. Note that the number 1000 only has 4 digits
"""
import logging


def fib_value_length(n: int = 1000) -> dict:
    """
    The function calculates the Fib series and returns the index
    and the value of the first number whose length is greater or
    equal to N.
    :param n:
            Maximum length of fib value
    :return:
            Dict with index and value

    """

    idx, current_value, last_value = 1, 1, 0
    while len(str(current_value)) <= n:
        idx += 1
        last_value, current_value = current_value, current_value + last_value

    return {'idx': idx, 'number': current_value}


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger.info(f'Starting...')
    logger.info(fib_value_length())
