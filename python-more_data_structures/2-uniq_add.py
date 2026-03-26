#!/usr/bin/python3
def uniq_add(my_list = []):
    total = 0
    for i in range(len(my_list)):
        if not my_list[i] in my_list[:i]:
            total += my_list[i]
    return total
