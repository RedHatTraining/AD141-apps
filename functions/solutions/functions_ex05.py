#!/usr/bin/env python3
"""Calculator application"""
def Add():
    val1 = input("Enter the first value to add: ")
    val2 = input("Enter the second value to add: ")
    print(val1," + ",val2,":",float(val1)+float(val2))

def Subtract():
    val1 = input("Enter the first value: ")
    val2 = input("Enter the value to subtract: ")
    print(val1," - ",val2,":",float(val1)-float(val2))

def Multiply():
    val1 = input("Enter the first value: ")
    val2 = input("Enter the value to multiply by: ")
    print(val1," * ",val2,":",float(val1)*float(val2))

def Divide():
    val1 = input("Enter the first value: ")
    val2 = input("Enter a non-zero value to divide by: ")
    print(val1," / ",val2,":",float(val1)/float(val2))

def illegal():
    print("Illegal Selection\n")

def Quit():
    exit()

menu = {"1": Add, "2": Subtract, "3": Multiply, "4": Divide, "5": Quit}
keys = sorted(menu.keys())
while True:
    print("Calulator Options:")
    for key in keys:
        print("\t", key, menu[key].__name__)
    key = input(">")

    menu.get(key, illegal)()
