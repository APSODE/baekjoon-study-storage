from sys import stdin


def fast_input() -> str:
    return stdin.readline().rstrip("\n")


drawing_paper = [[True for _ in range(100)] for _ in range(100)]

for _ in range(int(fast_input())):
    color_paper_leftdown_pos = list(map(int, fast_input().split(" ")))
    for y in range(10):
        for x in range(10):
            drawing_paper[color_paper_leftdown_pos[1] + y - 1][color_paper_leftdown_pos[0] + x - 1] = False


flatten_array = [drawing_paper[row][column] for column in range(100) for row in range(100)]
print(flatten_array.count(False))
