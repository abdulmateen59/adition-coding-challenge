"""
A rabbit wants to jump from one side of the road to the other. The rabbit starts at position A and wants to get to B.
For simplicity the rabbit can only jump a fixed distance D. Write an efficient function int jumps(int A, int B, int D)
that returns the minimal number of jumps required to get from A to B (or further in case the last jump makes the rabbit
jump over B).For example: givenA=10, B=85, D=30, the function should return 3. The first jump takes the rabbit to
10+30=40. The second jump to 40+30=70. The third jump to 70+30=100
"""
import logging


def jumps(a: int = 10, b: int = 85, d: int = 30) -> tuple[int, int]:
    """
    Calculates the number of jumps required to reach point b
    from point a using the distance d.
    :param a:
            Initial point
    :param b:
            Target point
    :param d:
            Max covering distance
    :return:
            Total jumps

    """
    if d <= 0:
        return 0, 0
    if a > b:
        a = b-1
    rabbit_jumps, total_dist = 0, a
    while total_dist < b:
        total_dist += d
        rabbit_jumps += 1

    return rabbit_jumps, total_dist


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger.info(f'Number of jumps: {jumps()[0]}, distance covered {jumps()[1]}')
