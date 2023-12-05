from sys import stdin


def fast_input() -> str:
    return stdin.readline().rstrip("\n")


user_input = list(map(int, fast_input().split(" ")))

N = user_input[0]
M = user_input[1]

baskets = [i + 1 for i in range(N)]

for _ in range(M):
    move_command = list(map(int, fast_input().split(" ")))
    sender_idx = move_command[0] - 1
    receiver_idx = move_command[1] - 1

    temp = baskets[receiver_idx]
    baskets[receiver_idx] = baskets[sender_idx]
    baskets[sender_idx] = temp

print(" ".join([str(i) for i in baskets]))
