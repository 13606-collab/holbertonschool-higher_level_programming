#!/usr/bin/python3
str=""
for i in range(90,64,-1):
    if i % 2 == 0:
        str+=chr(i+32)
    else:
        str+=chr(i)
print("{}".format(str))
