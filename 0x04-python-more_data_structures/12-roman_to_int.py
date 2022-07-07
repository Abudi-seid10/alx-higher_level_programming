#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    value = 0
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}

    if len(roman_string) == 1:
        return roman_dic[roman_string]

    for i in range(len(roman_string) - 1):
        if roman_dic[roman_string[i]] < roman_dic[roman_string[i + 1]]:
            roman_dic[roman_string[i]] = -(roman_dic[roman_string[i]])

    for j in roman_string:
        value += roman_dic[j]
    return value
