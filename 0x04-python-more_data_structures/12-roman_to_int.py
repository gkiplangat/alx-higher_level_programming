#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    numeral_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    if any(char not in numeral_values for char in roman_string):
        return 0

    result = numeral_values[roman_string[0]]

    for i in range(1, len(roman_string)):
        current_value = numeral_values[roman_string[i]]
        previous_value = numeral_values[roman_string[i-1]]

        if previous_value < current_value:
            result += current_value - 2 * previous_value
        else:
            result += current_value

    return result

