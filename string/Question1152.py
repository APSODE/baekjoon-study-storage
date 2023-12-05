from sys import stdin


def fast_input() -> str:
    return stdin.readline().rstrip("\n")


input_string_arr = fast_input().split(" ")

if input_string_arr[-1] == "":
    input_string_arr.pop(-1)

if input_string_arr[0] == "":
    input_string_arr.pop(0)

print(len(input_string_arr))

