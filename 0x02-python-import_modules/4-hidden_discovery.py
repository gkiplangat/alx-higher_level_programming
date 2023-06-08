#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    lists = [name for name in dir(hidden_4) if not name.startswith('__')]

    for name in sorted(lists):
        print(name)
