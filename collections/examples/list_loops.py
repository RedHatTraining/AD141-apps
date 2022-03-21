#!/usr/bin/env python3
numbers = [10, 20, 30, 40, 50]

# Looping by element
for number in numbers:
    print(number, end="\t")
print()

# Looping by index and
# updating list's values at the same time
for index in range(len(numbers)):
    numbers[index] *= 10

for number in numbers:
    print(number, end="\t")
print()
