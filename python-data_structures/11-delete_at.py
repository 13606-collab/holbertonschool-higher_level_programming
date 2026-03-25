#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in range(len(my_list)):
        if not i == idx:
            new_list.append(my_list[i])
    my_list[:] = new_list
    return new_list
