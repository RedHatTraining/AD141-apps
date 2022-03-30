#!/usr/bin/env python3
'''
json_ex1.py

Create a program that reads books.json.
Prompt a user to enter a book title until they decide to quit.
If the title is in the JSON data, print the data for that book.
If the book is not in the JSON data, the program should indicate as much.
'''

import json


def print_data(book, data):
    print(f"{book}:")
    for k, v in data.items():
        print(f"{k:>10}: {v}")


def main():
    with open("books.json", "r") as data:
        books = json.load(data)

    while True:
        book_to_find = input("Enter the title of a book (q to quit): ")
        if book_to_find.lower() == "q":
            print("Goodbye")
            break

        book = books.get(book_to_find)
        if book:
            print_data(book_to_find, book)
        else:
            print(book_to_find, "was not found")


if __name__ == "__main__":
    main()
