#!/usr/bin/python3
def islower(c):
    if ord(c) in range(91, 116):
        print("{} is upper".format(c))
    else:
        print("{} is lower".format(c))
islower(c="A")
