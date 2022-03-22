#!/usr/bin/env python3
def wrap_with_border(some_text):
    """ Returns a string of some_text with a line of # signs
        before and after it"""
    result = [len(some_text) * "#"]
    result.append(some_text)
    result.append(result[0])
    return "\n".join(result)


print("The doc string is:\n", wrap_with_border.__doc__)
