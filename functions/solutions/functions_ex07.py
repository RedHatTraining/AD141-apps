#!/usr/bin/env python3
"""Return the number of elements in a list greater than X"""
def get_count_greater_than(*the_list, num=0):
    results = filter(lambda x: x > num, the_list)
    return len(list(results))

test1 = "-1 2 -3 4 -5 6 -7 8 -9 10"
test_list = map(int, test1.split())
test2 = [5, -6, 7, -8]
test3 = (-9, 10, -11, 12)
test4 = {-10, 20, -30,40, -50, 60}
test5 = {"one":1, "two":2, "three":3, "negative_five": -5}
fmt = "The number of items greater than 2 from {} ==> {}"
print(fmt.format(test1, get_count_greater_than(*test_list, num=2)))
print(fmt.format(test2, get_count_greater_than(*test2, num=2)))
print(fmt.format(test3, get_count_greater_than(*test3, num=2)))
print(fmt.format(test4, get_count_greater_than(*test4, num=2)))
print(fmt.format(test5, get_count_greater_than(*test5.values(), num=2)))
print(fmt.format("5,-6,7", get_count_greater_than(5,-6,7, num=2)))
