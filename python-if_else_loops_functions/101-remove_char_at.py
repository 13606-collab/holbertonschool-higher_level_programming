#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ""
    count = 0
    for i in str:
        if count != n:
            str1 += i
        count += 1
    return str1
