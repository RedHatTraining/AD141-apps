#!/usr/bin/env python3
def volume(length, width, height):
    """Returns the volume of a box for given dimensions"""
    return length * width * height


dim1 = float(input("Enter length of the box: "))
dim2 = float(input("Enter width of the box: "))
dim3 = float(input("Enter height of the box: "))
result = volume(length=dim1, width=dim2, height=dim3)
print("The volume is:", result)

result = volume(height=dim3, length=dim1, width=dim2)
print("The volume is:", result)
