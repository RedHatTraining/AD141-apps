#!/usr/bin/env python3
indent = 0
text = "sum_to"


def sum_to(n):
    global indent
    print(" " * indent, text, n)
    indent += 1
    if not n:
        indent -= 1
        print(" " * indent, text, n, " => ", n)
        return n
    result = sum_to(n - 1)
    indent -= 1
    print(" " * indent, text, n, end="")
    print(" => {0:2} + {1:2} => {2:2}".format(n, result, n + result))
    return n + result


limit = 6
print("\nSum from 1 to", limit, "is:", sum_to(limit))
