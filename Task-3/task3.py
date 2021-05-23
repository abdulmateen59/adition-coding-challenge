"""
Integers in their binary representation contain 1s and 0s. For example 1001 in binary is 9 in decimal.
Write a function int zeroes(int i) that returns the largest number of consecutive 0s surrounded by 1s.
For example given i = 168000 (which is binary 101001000001000000) return 5. The last 6 zeroes are not
surrounded by 1s, since there is only a 1 to the left
"""
import logging
import re


def zeros_sequence(n: int = 168000) -> int:
    """
    The function calculates 0 run surrounded by 1
    :param n:
            Integer of binary
    :return:
            len of max sequence between consecutive 1's
    """

    return len(max(re.findall(r'1(?=(0+)1)', bin(n))))


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger.info(f'Number of zeros = {zeros_sequence()}')
    logger.info(f'Number of zeros = {zeros_sequence(n=9)}')
    logger.info(f'Number of zeros = {zeros_sequence(n=16901)}')
