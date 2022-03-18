#!/usr/bin/env python3
""" A Solution For language_ex07

    Use a range to loop through and print each number from 0 to 49
    to produce the following output.
        • Each number should be printed individually as opposed
          to concatenating them as a string.

 0   1   2   3   4   5   6   7   8   9
10  11  12  13  14  15  16  17  18  19
20  21  22  23  24  25  26  27  28  29
30  31  32  33  34  35  36  37  38  39
40  41  42  43  44  45  46  47  48  49
"""

for value in range(50):
    if value <= 9:
        print(" ", end="")
    print("", value, end="")
    if value % 10 == 9:
        print()

print()

# Printing again usingn formatted printing where
# {:3} indicates to pad with whitespace to 3 characters wide
fmt = "{:3}"
for value in range(50):
    print(fmt.format(value), end="")
    if value % 10 == 9:
        print()
