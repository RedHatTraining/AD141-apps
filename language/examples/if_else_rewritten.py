#!/usr/bin/env python3
number = int(input("Enter a number between 1 and 100: "))
target = 50
if number < target:
    result = "is less than"
else:
    result = "is greater than or equal to "

print(number, result, target)
