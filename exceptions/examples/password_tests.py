#!/usr/bin/env python3
from password_errors import PasswordError
from password_utilities import check_trivial, check_length, check_duplicates


def check_password(password):
    check_trivial(password)
    check_length(password)
    check_duplicates(password)


def main():
    while True:
        try:
            line = input("Please enter a password")
            check_password(line)
            print("That would be a valid password")
        except PasswordError as pe:
            print("Password Error: ", pe)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Terminating Program")
    except Exception as e:
        print("Unknown Issue:", e)
