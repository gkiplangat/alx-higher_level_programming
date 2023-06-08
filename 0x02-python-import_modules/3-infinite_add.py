#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum_of_arguments = 0
    arguments = sys.argv

    if len(arguments) > 1:
        for arg in sys.argv[1:]:
            sum_of_arguments += int(arg)

    print(sum_of_arguments)
