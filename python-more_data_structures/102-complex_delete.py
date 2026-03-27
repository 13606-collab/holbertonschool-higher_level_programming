#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return None
    new_dict = list(a_dictionary)
    for i in new_dict:
        if a_dictionary.get(i) == value:
            del a_dictionary[i]
    return a_dictionary
