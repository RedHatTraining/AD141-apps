#!/usr/bin/python3

print("We'll compare two integers in this script.\n") 
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

if a > b:
    print("Your first number is larger than your second number.")
elif b > a:
    print("Your second number is larger than your first number.")
else:
    print("These numbers are equal or an error occured.") 


