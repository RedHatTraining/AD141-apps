#!/usr/bin/env python3
"""Return the sum of numbers in a variable length argument"""
def sum_varargs(*the_list):
    sum = 0
    for item in the_list:
        sum += item

    return sum

test1 = "1 2 3 4 5 6 7 8 9 10"
test_list = map(int, test1.split())
test2 = [5, 6, 7, 8]
test3 = (9, 10, 11, 12)
test4 = {10, 20, 30,40, 50, 60}
test5 = {"one":1, "two":2, "three":3}
print("The sum of",test1,"is",sum_varargs(*test_list))
print("The sum of",test2,"is",sum_varargs(*test2))
print("The sum of",test3,"is",sum_varargs(*test3))
print("The sum of",test4,"is",sum_varargs(*test4))
print("The sum of",test5,"is",sum_varargs(*test5.values()))
print("The sum of 5,6,7 is",sum_varargs(5,6,7))
