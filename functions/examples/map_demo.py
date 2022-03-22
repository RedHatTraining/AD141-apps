#!/usr/bin/env python3
data = ["2", "4", "6", "8"]
values = map(int, data)
print(type(values), ":", values)
total = 0
for value in values:
    total += value
print("Sum of numbers in {} = {}".format(data, total))
