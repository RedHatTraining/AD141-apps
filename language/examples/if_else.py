#!/usr/bin/env python3
number = int(input("Enter a number between 1 and 100: "))
target = 50
if number < target:
    print(number, "is less than", target)
else:
    print(number, "is greater than or equal to ", target)
