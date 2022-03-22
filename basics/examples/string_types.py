#!/usr/bin/env python3
print("AbCDe".isalpha(), "AbCd123".isalpha())   # True False
print("123".isnumeric(), "12.3".isnumeric())    # True False
print("  \t\n".isspace(), "a b\t\n".isspace())  # True False
print("ABCD".isupper(), "abcd".isupper())       # True False
