#!/usr/bin/env python3
from customer_functions import get_customers


def main():
    customer_list = get_customers()
    customer_list.sort(key=lambda x: (x[4], x[1], x[0]))
    for customer in customer_list:
        print(customer)


if __name__ == "__main__":
    main()
