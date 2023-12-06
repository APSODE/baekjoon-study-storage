from sys import stdin
from math import isqrt


def fast_input() -> str:
    return stdin.readline().rstrip("\n")


def calc_dot_amount(loop_amount: int, before_amount: int = 4) -> int:
    if loop_amount > 0:
        side_dot_amount = isqrt(before_amount)

        next_side_dot_amount = 2 * side_dot_amount - 1
        next_dot_amount = next_side_dot_amount ** 2

        return calc_dot_amount(loop_amount - 1, before_amount = next_dot_amount)

    else:
        return before_amount


print(calc_dot_amount(int(fast_input())))
