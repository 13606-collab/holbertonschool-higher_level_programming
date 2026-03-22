#!/usr/bin/python3
def print_last_digit(number):
    if number%10 == 0:
        print(0)
    else:
        print(abs(number)%10)
