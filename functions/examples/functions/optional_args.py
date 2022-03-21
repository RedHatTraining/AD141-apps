#!/usr/bin/env python3
def volume(length=10, width=5, height=2):
    """Returns the volume of a box for given dimensions"""
    return length * width * height


print("1:", volume(2, 3, 4))
print("2:", volume(2, 3))
print("3:", volume(2))
print("4:", volume())

vol = volume(30, height=4, width=20)
print("5:", vol)

print("6:", volume(height=3))
print("7:", volume(height=7, width=2))
