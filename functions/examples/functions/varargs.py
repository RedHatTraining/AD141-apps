#!/usr/bin/env python3
def modify(qty, *values, end="\n"):
    for val in values:
        print(qty * val, end=end)


modify(3, "Hello", "Bye", "Sample", end="|")
print()
modify(4, 10, 20, 30, end=" ~ ")
print()
modify(15, 2, 3, 4)
