#!/usr/bin/env python3
""" A Solution For language_ex03

    Write a program that prompts twice for an integer.
    • The program should print the larger of the two numbers.
    • If the numbers are equal, the program should indicate it as such.
"""
prompt = "Enter {} whole number: "
first = int(input(prompt.format("a")))
second = int(input(prompt.format("a second")))

larger_text = "is the larger number"
if first < second:
    print(second, larger_text)
elif first > second:
    print(first, larger_text)
else:
    print("The numbers are equal")
