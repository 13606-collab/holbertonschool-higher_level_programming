#!/usr/bin/python3
def uppercase(c):
    strc = ""
    for i in c:
        if ord(i) in range(65, 91):
            strc += str(i)
        elif ord(i) in range(97, 123):
            strc += chr(ord(i)-32)
        else:
            strc += i
    print("{}".format(strc))
