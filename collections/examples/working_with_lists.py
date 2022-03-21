#!/usr/bin/env python3
numbers = [10, 20, 30, 40, 20, 50]
fmt = "{0:>24} {1}"
print(fmt.format("Original:", numbers))
print(fmt.format("Pop Last Element:", numbers.pop()))
print(fmt.format("Pop Element at pos# 2:", numbers.pop(2)))
print(fmt.format("Resulting List:", numbers))

numbers.append(100)
print(fmt.format("Appended 100:", numbers))
numbers.remove(20)
print(fmt.format("Removed First 20:", numbers))
numbers.insert(1, 1000)
print(fmt.format("Inserted 1000 at pos# 1:", numbers))

numbers.reverse()
print(fmt.format("Reversed:", numbers))
numbers.sort()
print(fmt.format("Sorted:", numbers))
numbers[0] = -99
print(fmt.format("Modified:", numbers))
