from sys import stdin


def fast_input() -> str:
    return stdin.readline().rstrip("\n")


for i in range(int(fast_input())):
    input_string = fast_input()
    print(f"{input_string[0]}{input_string[-1]}")


