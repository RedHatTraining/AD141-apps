#!/usr/bin/env python3
""" A Solution For functions_ex05
    Write a calculator application that presents the following menu:
        Calculator options:
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Quit
    • The user is expected to enter a number from the above menu.
    • After choosing the operation, the user should be prompted twice for
      2 numbers and the chosen operation performed on them with the result
      being displayed on the screen.
    • Each of the above options should be implemented as its own function.
"""


def get_values():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    return (x, y)


def add():
    x, y = get_values()
    print(f"{x}+{y}={x+y}\n")


def subtract():
    x, y = get_values()
    print(f"{x}-{y}={x-y}\n")


def multiply():
    x, y = get_values()
    print(f"{x}*{y}={x*y}\n")


def divide():
    x, y = get_values()
    print(f"{x}/{y}={x/y:.2f}\n")


def quit():
    print("Exiting...")
    exit()


def not_an_option():
    print("This calculator can't do that...\n")


calc = {"1": add, "2": subtract, "3": multiply, "4": divide, "5": quit}
while True:
    print("Calculator Options:")
    for key in calc:
        print(f"{key}. {calc[key].__name__.capitalize()}")
    choice = input("Choose an action: ")

    calc.get(choice, not_an_option)()
