#!/usr/bin/env python3
from customer_and_address import Address, Customer


def get_customers():
    customer_list = []
    with open("customers.txt", "r") as thefile:
        for customer_txt in thefile:
            c = customer_txt.rstrip().split(",")
            address = Address(c[2], c[3], c[4], c[5])
            customer = Customer(c[0], c[1], address)
            customer_list.append(customer)
    return customer_list


def sortby(customer):
    return (customer.address.state, customer.last_name, customer.first_name)


def main():
    customer_list = get_customers()
    customer_list.sort(key=sortby)
    for customer in customer_list:
        print(customer, end="\n\n")


if __name__ == "__main__":
    main()
