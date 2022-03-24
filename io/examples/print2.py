#!/usr/bin/env python3
def main():
    with open("output", "w") as a_file:
        while True:
            data = input("Enter data ('q' to exit): ")
            if data == "q":
                break
            print(data, file=a_file)

    print("File Is Now Closed? ", a_file.closed)


if __name__ == "__main__":
    main()
