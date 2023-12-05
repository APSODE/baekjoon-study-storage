from sys import stdin


def fast_input() -> str:
    return stdin.readline().rstrip("\n")


print(sum([i**2 for i in list(map(int, fast_input().split(" ")))]) % 10)