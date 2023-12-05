from sys import stdin


def fast_input() -> str:
    return stdin.readline().rstrip("\n")

MAX = 0
TURN = 1
for turn in range(1, 10):
    current_num = int(fast_input())

    if current_num >= MAX:
        MAX = current_num
        TURN = turn

print(MAX)
print(TURN)
