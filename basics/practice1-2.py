#!/usr/bin/python3

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
full_name = "Your full name is: " + first_name + " " + last_name
initials = "Your initials are: " + first_name[0].capitalize() + last_name[0].capitalize()

print(full_name)
print(initials)
