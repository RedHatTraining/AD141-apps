#!/usr/bin/python3

lucky = input("Enter a lucky number: ")

#Improper use of operator. 
#if lucky is int: 
#    print("It's your lucky number: " + lucky + "!")
#else:
#    print("That's not a number! Enter an integer.")

if lucky.isnumeric() == True:
    print("It's your lucky number: " + lucky + "!")
else:
    print("That's not a number! Enter an integer.")
