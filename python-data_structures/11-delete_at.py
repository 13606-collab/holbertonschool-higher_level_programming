#!/usr/bin/python3
def delete_at(my_list=[1,2,3,4,5], idx=9):
    new_list = []
    if idx < 0 or idx >= len(my_list):
        new_list[:] = my_list
        return new_list
    for i in range(len(my_list)):
        if not i == idx:
            new_list.append(my_list[i])
    return new_list
print(delete_at())
