from sys import stdin
from typing import Tuple


def fast_input() -> str:
    return stdin.readline().rstrip("\n")


def get_changes_amount(input_change: int) -> Tuple[int, int, int, int]:
    changes = [0, 0, 0, 0]
    if input_change // 25 > 0:
        changes[0] = input_change // 25
        input_change %= 25

    if input_change // 10 > 0:
        changes[1] = input_change // 10
        input_change %= 10

    if input_change // 5 > 0:
        changes[2] = input_change // 5
        input_change %= 5

    changes[3] = input_change

    return changes[0], changes[1], changes[2], changes[3]


T = int(fast_input())
for _ in range(T):
    user_change = int(fast_input())
    print(" ".join(map(str, get_changes_amount(user_change))))
