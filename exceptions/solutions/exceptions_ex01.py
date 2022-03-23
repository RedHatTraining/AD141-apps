#!/usr/bin/env python3
""" A Solution For exceptions_ex01
    Create a list in your program that has 10 numbers.
    • Then, in a loop, ask the user for a number.
    • Use this number as an index into your list and print the value located
      at that index.
    • End the program when the user enters "end."
    • Handle the case of an illegal number.
    • Handle the case of an illegal subscript.
"""


def main():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        try:
            result = get_a_number()
        except ValueError:
            print("result is not an integer")
            continue

        if result is None:
            break    # End of program

        try:
            print(array[result])
        except IndexError:
            print("index out of range")


def get_a_number():
    result = input("Enter a number or 'end' to end the program: ")
    if result == "end":
        return None
    return int(result)


if __name__ == "__main__":
    main()
