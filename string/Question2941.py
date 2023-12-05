from sys import stdin
from typing import List


def fast_input() -> str:
    return stdin.readline().rstrip("\n")


input_string = fast_input()

amount = 0
croatian_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for c_alpha in croatian_alphabet:
    if c_alpha in input_string:
        amount += input_string.count(c_alpha)
        input_string = input_string.replace(c_alpha, " ")
amount += len(input_string.replace(" ", ""))

print(amount)
