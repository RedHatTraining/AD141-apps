#!/usr/bin/env python3
def main():
    words = ["hello", "racecar", "eye", "bike", "stats", "civic"]
    palindromes = [x for x in words if x[::-1] == x]
    print(palindromes)


if __name__ == "__main__":
    main()
