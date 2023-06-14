#!/usr/bin/python3

def search_replace(my_list, search, replace):
    my_new_list = my_list.copy()
    for i, item in enumerate(my_new_list):
        if item == search:
            my_new_list[i] = replace
    return my_new_list
