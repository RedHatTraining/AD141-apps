#!/usr/bin/env python3
def outer(a, b):
    x = 15
    y = 20

    return lambda z: print(a, b, x, y, z)


result = outer(5, 10)
print(type(result))
result(9)  # invoke the returned function
