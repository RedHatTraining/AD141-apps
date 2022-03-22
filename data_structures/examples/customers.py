#!/usr/bin/env python3
import customer_functions


def main():
    customer_list = customer_functions.get_customers()
    customer_functions.get_info(customer_list)
    customer_map = customer_functions.get_dictionary(customer_list)
    customer_functions.print_customernames(customer_map.keys())
    customer_functions.user_interaction(customer_map)


if __name__ == "__main__":
    main()
