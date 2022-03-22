#!/usr/bin/env python3
""" A Solution For basics_ex08
    Write a program that prompts the user twice for a number.
    • The first number will be the base, and the second number will be the
      exponent.
    • Print the result of raising the base to the exponent.
"""

base = float(input("enter a base: "))
exponent = float(input("enter an exponent: "))

result = base ** exponent

print(base, "to the", exponent, "power is", result)
