#!/usr/bin/python3

print("We'll add a range of integers in this script.\n") 
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
sum = 0

print("Adding up the following numbers: ") 

if a > b:
    for i in range (b, a+1, 1):
        print(i)
        sum = sum + i

elif a < b: 
    for i in range (a, b+1, 1):
        print(i)
        sum = sum + i

else: 
    print("You entered the same number or an error occurred. Output will default to zero and produce an error.")

print("For a total of: " + str(sum))
