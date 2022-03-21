#!/usr/bin/env python3
""" A Solution For language_ex06

    Ask the user to input three numbers representing a lower limit,
        a higher limit, and a step value.
    • The program should use a range object to loop through and print
      the numbers from low to high, taking into consideration the step.
"""
low = int(input("Enter a lower limit: "))
high = int(input("Enter an upper limit: "))
step = int(input("Enter a step size: "))

for i in range(low, high + 1, step):
    print(i)
