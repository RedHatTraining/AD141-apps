#!/usr/bin/env python3
def get_data():
    the_list = []
    while True:
        data = input("Enter data ('q' to exit): ")
        if data == "q":
            break
        the_list.append(data)
    return the_list


def main():
    data = get_data()
    f = open("output", "a")
    f.writelines(data)
    f.close()


if __name__ == "__main__":
    main()
