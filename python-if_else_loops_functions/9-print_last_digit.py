#!/usr/bin/python3
def print_last_digit(number):
    if number%10 == 0:
        return (0)
    else:
        return (abs(number)%10)
