from sys import stdin

"""
== ex input ==
9
ENTER
pjshwa
chansol
chogahui05
lms0806
pichulia
r4pidstart
swoon
tony9402

== ex output ==
8
"""


def fast_input() -> str:
    return stdin.readline().rstrip("\n")


input_amount = int(fast_input())
total_amount = 0

gomgom_use_history = set()

for currnent_turn in range(input_amount):
    user_input = fast_input()

    if user_input == "ENTER":
        total_amount += len(gomgom_use_history)
        gomgom_use_history = set()

    else:
        gomgom_use_history.add(user_input)


total_amount += len(gomgom_use_history)

print(total_amount)
