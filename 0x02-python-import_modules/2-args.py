#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv

    if len(args) == 1:
        print("0 arguments.")
    elif len(args) == 2:
        print("1 argument:")
    elif len(args) > 2:
        print(f"{len(args) - 1} arguments:")

    if len(args) > 1:
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"{i}: {arg}")
