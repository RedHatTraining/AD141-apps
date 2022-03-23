#!/usr/bin/env python3
""" A Solution For exceptions_ex02
    Test exceptions_ex01 again by using a few negative numbers as the index.
    • Eliminate negative numbers as legitimate subscripts by raising the
      IndexError exception when a negative number is given.
"""


def main():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        try:
            result = get_a_number()
        except ValueError:
            print("result is not an integer")
            continue
        except IndexError as ie:
            print(ie)
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
    number = int(result)
    if number < 0:
        raise IndexError(f"Negative indexes not allowed: {number}")
    return int(result)


if __name__ == "__main__":
    main()
