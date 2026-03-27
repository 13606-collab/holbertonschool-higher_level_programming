#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for i in a_dictionary:
        if a_dictionary.get(i) == value:
            new_dict.pop(i)
    return new_dict
