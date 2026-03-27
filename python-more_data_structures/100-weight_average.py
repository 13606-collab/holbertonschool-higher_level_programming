#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    toplam = 0
    w = 0
    for i in my_list:
        toplam += i[0]*i[1]
        w += i[1]
    return toplam/w
