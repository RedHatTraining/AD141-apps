#!/usr/bin/env python3
from numbers_and_math import math_examples, decimal_examples, random_examples


def main():
    examples = [math_examples, decimal_examples, random_examples]
    for function in examples:
        print(function.__name__.upper(), "*" * 50)
        function()


if __name__ == "__main__":
    main()
