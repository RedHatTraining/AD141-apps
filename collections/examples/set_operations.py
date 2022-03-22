#!/usr/bin/env python3
a, b = [set('efgy'), set('exyz')]
fmt = "Set a:{}\t\tSet b:{}"
tab = "\t"
print("The following operators return a new set")
print("Leaving the original two sets unchanged")
print(fmt.format(a, b))
print(tab, "a | b:", a | b)  # union
print(tab, "a & b:", a & b)  # intersection
print(tab, "a - b:", a - b)  # difference
print(tab, "b - a:", b - a)  # difference
print(tab, "a ^ b:", a ^ b)  # symmetric difference
print(fmt.format(a, b))
print("\n", "*" * 75)

print("\nThe '|=' operator modifies the original set")
a, b = [set('efgy'), set('exyz')]
a |= b
print(tab, "a |= b:", a)  # union
print(fmt.format(a, b))
