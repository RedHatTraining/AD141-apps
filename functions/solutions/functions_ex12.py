#!/usr/bin/env python3
"""Update dictionary values"""
def update_dictionary(value, the_dict):

    for key in the_dict.keys():
        the_dict[key] += value

test = {"A":1, "B":2, "C":3}
print("before: ", test)
update_dictionary(10, test)
print("after: ", test)
