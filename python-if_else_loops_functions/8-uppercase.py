#!/usr/bin/python3
def uppercase(c):
    for i in str(c):
        if ord(i) in range (65, 91):
            print(i, end = "")
        elif ord(i) in range (97, 123):
            print(chr(ord(i)-32), end = "")
        else:
            print(i, end = "")
