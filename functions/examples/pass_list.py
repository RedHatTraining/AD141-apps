#!/usr/bin/env python3
def multiply_by(qty, a_list):
    for index, value in enumerate(a_list):
        a_list[index] = value * qty


def process_list(a_list):
    print("Before:", a_list)
    multiply_by(5, a_list)
    print("After:", a_list)


data = [10, 20, 30, 40]
process_list(data)

data = ["Me", "the", "Hello"]
process_list(data)
