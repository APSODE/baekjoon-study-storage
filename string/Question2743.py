from sys import stdin


def fast_input() -> str:
    return stdin.readline().rstrip("\n")


print(len(fast_input()))
