#!/usr/bin/env python3
"""Return the sum and average of numbers in a variable length argument"""
def sum_avg_varargs(*the_list):
    sum = 0
    count = 0
    for item in the_list:
        sum += item
        count += 1

    return (sum, sum/count)

test1 = "1 2 3 4 5 6 7 8 9 10"
test_list = map(int, test1.split())
test2 = [5, 6, 7, 8]
test3 = (9, 10, 11, 12)
test4 = {10, 20, 30,40, 50, 60}
test5 = {"one":1, "two":2, "three":3}
fmt = "The sum and average of {} ==> {}"
print(fmt.format(test1, sum_avg_varargs(*test_list)))
print(fmt.format(test2, sum_avg_varargs(*test2)))
print(fmt.format(test3, sum_avg_varargs(*test3)))
print(fmt.format(test4, sum_avg_varargs(*test4)))
print(fmt.format(test5, sum_avg_varargs(*test5.values())))
print(fmt.format("5,6,7", sum_avg_varargs(5, 6,7)))
