from sys import stdin


def fast_input() -> str:
    return stdin.readline().rstrip("\n")


input_string = fast_input()
print(input_string[int(fast_input()) - 1])