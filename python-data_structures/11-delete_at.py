#!/usr/bin/python3
def delete_at(my_list=[1,2,3,4,5], idx=3):
    if idx <= 0:
        return my_list
    new_list = []
    for i in range(len(my_list)):
        if not i == idx:
            new_list.append(my_list[i])
    return new_list
