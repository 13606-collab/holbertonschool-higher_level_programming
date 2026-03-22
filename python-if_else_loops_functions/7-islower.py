#!/usr/bin/python3
def islower(c):
    if ord(c) in range(91, 116):
        print("{} is lower".format(c))
    else:
        print("{} is upper".format(c))
islower(c="A")
