#!/usr/bin/env python3
def get_customers():
    with open("customers.txt", "r") as thefile:
        customer_list = thefile.readlines()
    # use a list comprehension to convert to a
    # nested list of lists (each a list of strings)
    return [customer.rstrip().split(",") for customer in customer_list]


def get_info(customers):
    print("Nested Structure:", type(customers),
          type(customers[0]), type(customers[0][0]))
    # partial contents of customers
    print(customers[0], customers[1], sep="\n", end="\n\n")


def get_dictionary(customers):
    # Convert to dictionary using a dictionary comprehension
    return {"{} {}".format(cust[0], cust[1]): cust for cust in customers}


def print_customernames(customer_names):
    print("Customer names:")
    for i, name in enumerate(customer_names):
        print("{0:20}".format(name), end="|")
        if i % 4 == 3:
            print()
    print("\n")


def user_interaction(customers):
    tags = ["FirstName", "LastName", "Street", "City", "State", "ZipCode"]
    fmt = "{:16}{:16}{:20}{:16}{:6}{:5}"
    while True:
        name = input("Enter a name (or 'quit' to quit):")
        if name == "quit":
            break
        data = customers.get(name)
        if data:
            print(fmt.format(*tags))
            print(fmt.format(*data))
