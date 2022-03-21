#!/usr/bin/env python3
"""Test that an integer input is positive"""
def validate_positive_int():
    value = int(input("Please enter a positive integer:"))
    if value < 0:
        return 0
    else:
        return value

while True:
    result = validate_positive_int()
    if result == 0:
        break

invalid_text = "Either zero or An invalid entry was given"    
print("-" * len(invalid_text))
print(invalid_text)
print("-" * len(invalid_text))
