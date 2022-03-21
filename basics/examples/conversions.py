#!/usr/bin/env python3
# conversions to an integer
result = input("Please enter an integer: ")
number = int(result)
print("Your number plus 10 equals:", number + 10)
print("String of", result, "converted to various bases as int:")
fmt = "Base 10: {}\tBase 2: {}\tBase 8: {}\tBase 16: {}"
print(fmt.format(int(result), int(result, 2), int(result, 8), int(result, 16)))
print()
# conversions to a float
a_float = input("Please enter a decimal number: ")
sum_of_input = float(a_float) + float(result)
print(a_float, "+", result, "=", sum_of_input)
print()
print(number, "as string in the following bases:")
fmt = "Binary: {}\tOctal: {}\tHex: {}"
print(fmt.format(bin(number), oct(number), hex(number)))

print('ord("A") =', ord("A"), '     chr(66) =', chr(66))

print("The sum of the input equals", sum_of_input)
