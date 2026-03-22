#!/usr/bin/python3
def print_last_digit(number):
    if number%10 == 0:
        print(0)
    elif number >= 0:
        print(number%10)
    else:
        print(10-number%10)
