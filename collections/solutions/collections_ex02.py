#!/usr/bin/env python3
""" A Solution For collections_ex02
    Write a program that creates a loop asking the user to input a number.

        • Repeat this process until the user enters the value `end`.
        • The following can be used to loop through the user input.

----
prompt = "Enter a number (or the word 'end' to quit) "
while True:
    data = input(prompt)
    if data == "end":
        break
    #Remainder of while loop goes here
----

    • Add each iteration number to a `list`.

    • Just before the program ends, print the following:
        • The contents of the list on one line
        • The sum of the elements in the list on the second line.
"""

numbers = []
prompt = "Enter a number (or the word 'end' to quit) "
while True:
    data = input(prompt)
    if data == "end":
        break
    numbers.append(int(data))

print("The list is:", numbers)
total = 0
for value in numbers:
    total += value
print("The sum of the numbers is:", total)
