#!/usr/bin/python3
""" Peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Returns: peak of list_of_integers or None"""
    listLength = len(list_of_integers)
    midA = listLength
    mid = listLength // 2

    if listLength == 0:
        return None

    while True:
        midA = midA // 2
        if (mid < listLength - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if midA // 2 == 0:
                midA = 2
            mid = mid + midA // 2
        elif midA > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if midA // 2 == 0:
                midA = 2
            mid = mid - midA // 2
        else:
            return list_of_integers[mid]