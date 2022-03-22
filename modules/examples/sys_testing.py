#!/usr/bin/env python3
import sys


def main():
    print("Script Name:", sys.argv.pop(0))
    print("Remaining Command Line Arguments:", sys.argv)

    info = sys.version_info
    print("Python Version:")
    print(info.major, info.minor, info.micro, sep=".")

    print("Python Path:")
    for each_path in sys.path:
        print("\t", each_path)
    print()

    number = input("Please enter an integer")
    if not number.isdecimal():
        sys.exit(number + " is not an integer.")

    print("You entered the number " + number)


if __name__ == "__main__":
    main()
