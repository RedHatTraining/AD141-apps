#!/usr/bin/env python3

""" A Solution For basics_ex05
    Write an application that prompts to enter the radius of a circle.
    • Accept the user input into a variable.
    • Compute and print the area of the circle whose radius was input.
    • The formula for the area of a circle is πr²
          (pi times the square of the radius).
    • Use 3.14159 for pi.
"""
pi = 3.14159
radius = float(input("Enter the radius of the circle: "))
area = pi * radius ** 2
print("The area of circle with radius", radius, "is", area)
