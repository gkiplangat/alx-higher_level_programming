#!/usr/bin/python3
def uppercase(str):
    upper_str = []
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            upper_str.append(chr(ord(c) - 32))
        else:
            upper_str.append(c)
    new_string = "".join(upper_str)
    print("{}".format(new_string))
