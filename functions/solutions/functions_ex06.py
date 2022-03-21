#!/usr/bin/env python3
"""Return the positive elements in a list"""
def get_positives(*the_list):
    results = filter(lambda x: x > -1, the_list)
    return list(results)

test1 = "-1 2 -3 4 -5 6 -7 8 -9 10"
test_list = map(int, test1.split())
test2 = [5, -6, 7, -8]
test3 = (-9, 10, -11, 12)
test4 = {-10, 20, -30,40, -50, 60}
test5 = {"one":1, "two":2, "three":3, "negative_five": -5}
fmt = "The positive items of {} ==> {}"
print(fmt.format(test1, get_positives(*test_list)))
print(fmt.format(test2, get_positives(*test2)))
print(fmt.format(test3, get_positives(*test3)))
print(fmt.format(test4, get_positives(*test4)))
print(fmt.format(test5, get_positives(*test5.values())))
print(fmt.format("5,-6,7", get_positives(5,-6,7)))
