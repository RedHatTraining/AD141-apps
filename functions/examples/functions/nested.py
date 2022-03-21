#!/usr/bin/env python3
def outer(a, b):
    x = 15
    y = 20

    def inner(z):
        print(a, b, x, y, z)

    return inner  # a reference to inner function


result = outer(5, 10)
print(type(result))
result(9)  # invoke the returned function
