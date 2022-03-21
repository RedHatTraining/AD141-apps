#!/usr/bin/env python3
value = int(input("Please enter a whole number: "))

print(value, end=" is ")
if value <= 5:
    print("less than or equal to 5")
elif value <= 10:
    print("between 6 and 10 inclusively")
elif value <= 15:
    print("between 11 and 15 inclusively")
else:
    print("greater than 15")

print("This statement is not part of the above if else")
