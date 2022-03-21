#!/usr/bin/env python3
"""Return the length of the longest string in the collection"""
def len_longest_str(the_list):
    value = 0
    for item in the_list:
        if len(item) > value:
            value = len(item)

    return value

test = "This is not a test of the emergency broadcast system"
test_list = test.split()
longest_word = len_longest_str(test_list)
fmt = "{:>" + str(longest_word) + "}"
for word in test_list:
    print(fmt.format(word))
