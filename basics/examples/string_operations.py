#!/usr/bin/env python3
# The concatenation operator (+)
first_name = "Casey"
last_name = "Jackson"
full_name = first_name + " " + last_name
print(full_name)  # Casey Jackson

# Note the automatic string concatenation below
fullName = "Casey" " " "Jackson"
print(fullName)

# The asterisk (*) operator
stars = "*" * 12
pounds = 5 * "#"
print(stars, ":", pounds)  # ************ : #####

# The in operator is convenient for membership tests
x = "Hello there"
print('t' in x, 'ell' in x, 'hell' in x)  # True True False
