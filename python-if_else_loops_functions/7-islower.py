#!/usr/bin/python3
def islover(c):
    if ord(c) in range(65, 91):
        print("{} is upper".format(c))
    else:
        print("{} is lover".format(c))
islover(c="A")
