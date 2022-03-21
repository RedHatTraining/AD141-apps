#!/usr/bin/env python3
def square(p):
    return p * p


def increment(p):
    return p + 1


def compute(func, lis):
    for index, item in enumerate(lis):
        lis[index] = func(item)


data = [10, 20, 30, 40]
compute(square, data)
print(data)
compute(increment, data)
print(data)
