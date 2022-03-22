#!/usr/bin/env python3
def add():
    val = input("Enter value to add: ")
    data.append(val)


def delete():
    item = data.pop(0)
    print("removing", item)


def display():
    print("displaying:", data)


def terminate():
    print("terminating")
    exit()


def illegal():
    print("Illegal Selection\n")


data = []
menu = {"1": add, "2": delete, "3": display, "4": terminate}
keys = sorted(menu.keys())
while True:
    print("Make selection:")
    for key in keys:
        print("\t", key, menu[key].__name__)
    key = input(">")

    menu.get(key, illegal)()
