#!/usr/bin/env python3
""" A Solution For basics_ex06
    Write a program that prompts twice for an integer.
    • Print the product of the two numbers.
    • Once this works properly, try entering numbers with a decimal point.
    • What happens? Why?
    • Now try entering data that is non-numeric.
    • What happens? Why?
"""
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
product = first * second

print("Product of", first, "and", second, "is", product)

# Entering a number with a decimal point will cause the int()
#     constructor to raise an exception
# Could rewrite to call the float constructor instead.
#     first = float(input("enter first number: "))
#     second = float(input("enter second number: "))

# Entering any non-numeric data will cause the int and/or
#     float constructor(s) to raise an exception
