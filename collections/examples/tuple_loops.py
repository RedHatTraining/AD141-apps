#!/usr/bin/env python3
grades = ("A", "B", "C", "D", "F")
points = ("90-100", "80-89", "70-79", "60-69", "00-59")
for grade in grades:
    print(grade, end="\t")
print()

for a_tuple in enumerate(grades):
    print(a_tuple[0], ":", a_tuple[1], end="\t")
print()

# Unpacking the tuple from enumerate
for i, grade in enumerate(grades, start=1):
    print(i, ":", grade, end="\t")
print()

# Process the two tuples in parallel
for index, grade in enumerate(grades):
    print(grade, ":", points[index])
