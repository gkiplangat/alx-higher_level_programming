#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = [0, 0]
    j = [0, 0]

    if len(tuple_a) >= 2:
        i = tuple_a[:2]
    elif len(tuple_a) == 1:
        i[0] = tuple_a[0]

    if len(tuple_b) >= 2:
        j = tuple_b[:2]
    elif len(tuple_b) == 1:
        j[0] = tuple_b[0]

    return tuple((i[x] + j[x]) for x in range(2))
