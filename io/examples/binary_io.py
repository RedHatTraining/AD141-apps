#!/usr/bin/env python3
def main():
    text = "This is a string of data to be written\n"
    some_bytes = b"This should also be written to the file\n"
    a_byte_aray = bytearray("Hello", "utf-8")
    more_bytes = bytes("\nConverting this to bytes", "ascii")
    try:
        # Write to the file
        with open("binarydata", "wb") as the_file:
            print("Type of stream:", type(the_file).__name__)
            print("Module:", type(the_file).__module__)
            the_file.write(text.encode())
            the_file.write(some_bytes)
            the_file.write(a_byte_aray)
            the_file.write(more_bytes)

        # Read from the file
        with open("binarydata", "rb") as the_file:
            buffer = b''
            while True:
                the_text = the_file.read(10)
                if not the_text:
                    break
                buffer += the_text
        print(buffer)
        print("*" * 50)
        print(buffer.decode())
    except OSError as err:
        print("OS Error:", err)


if __name__ == "__main__":
    main()
