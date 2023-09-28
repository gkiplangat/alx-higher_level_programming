#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Finds & Returns peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    wholeList = len(list_of_integers)
    if wholeList == 1:
        return list_of_integers[0]
    elif wholeList == 2:
        return max(list_of_integers)

    middle = int(wholeList / 2)
    peak = list_of_integers[middle]
    if peak > list_of_integers[middle - 1] and peak > list_of_integers[middle + 1]:
        return peak
    elif peak < list_of_integers[middle - 1]:
        return find_peak(list_of_integers[:middle])
    else:
        return find_peak(list_of_integers[middle + 1:])
