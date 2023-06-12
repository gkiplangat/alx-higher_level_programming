#!/usr/bin/python3

def no_c(my_string):
    characters = [ch for ch in my_string if ch.lower() not in "Cc"]
    return ''.join(characters)
