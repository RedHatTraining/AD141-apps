#!/usr/bin/env python3
from fraction import Fraction


def main():
    try:
        while True:
            numer = int(input("Please enter a numerator"))
            denom = int(input("Please enter a denominator"))
            fraction = Fraction(numer, denom)
            print(fraction)
    except ZeroDivisionError:
        print("Zero Division Error")


if __name__ == "__main__":
    main()
