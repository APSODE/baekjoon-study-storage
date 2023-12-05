from sys import stdin


def fast_input() -> str:
    return stdin.readline().rstrip("\n")


dial_dict = {
    "ABC": 2,
    "DEF": 3,
    "GHI": 4,
    "JKL": 5,
    "MNO": 6,
    "PQRS": 7,
    "TUV": 8,
    "WXYZ": 9
}


total_time = 0
for user_input_char in fast_input():
    for key_string in dial_dict:
        if user_input_char in key_string:
            total_time += dial_dict.get(key_string) + 1

print(total_time)
