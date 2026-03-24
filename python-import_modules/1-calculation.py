#!/usr/bin/python3
from calculator import add
from calculator import sub
from calculator import mul
from calculator import div

if __name__ == "__main__":
    a = 10
    b = 5
    
    print("{} + {} = {}".format(a, b, add(a,b)))
    print("{} - {} = {}".format(a, b, add(a,b)))
    print("{} * {} = {}".format(a, b, add(a,b)))
    print("{} / {} = {}".format(a, b, add(a,b)))
