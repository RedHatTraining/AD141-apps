#!/usr/bin/env python3
import re


def main():
    text = "The numbers 123 and 57 are odd while 948 and 2800 are even"
    numbers = re.findall(r"\d+", text)
    print(numbers)

    result = re.sub(r"(\d+)", "#\\1", text)
    print(result)

    result = re.sub(r"(\d+)", r"#\1", text)
    print(result)


if __name__ == "__main__":
    main()
