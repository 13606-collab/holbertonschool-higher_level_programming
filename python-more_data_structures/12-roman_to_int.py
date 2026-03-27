#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0
    before = 1000
    for i in roman_string:
        if i not in roman:
            return 0
        if roman.get(i) > before:
            integer = (integer + roman.get(i) - 2 * before)
        else:
            integer += roman.get(i)
        before = roman.get(i)
    return integer
