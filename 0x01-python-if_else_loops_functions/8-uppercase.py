#!/usr/bin/python3
def uppercase(str):
    uppercase_chars = []
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_chars.append(chr(ord(char) - 32))
        else:
            uppercase_chars.append(char)
    new_string = "".join(uppercase_chars)
    print("{}".format(new_string))

# Test the function
uppercase("Hello, World!")

