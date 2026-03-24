#!/usr/bin/python3
import sys
if __name__ == "__main__":
    
    s = 0
 
    for i in sys.argv[1:]:
        s += int(i)

     print("{}".format(s), end = "\n")
