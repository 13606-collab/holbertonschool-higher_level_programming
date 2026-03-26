#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = sorted(a_dictionary)
    for i in new_list:
        print([i,a_dictionary[i]])
