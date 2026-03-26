#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = []
    for i in set_1:
        if not i in set_2:
            set_3.append(i)
    for i in set_2:
        if not i in set_1:
            set_3.append(i)
    return sorted(set(set_3))
