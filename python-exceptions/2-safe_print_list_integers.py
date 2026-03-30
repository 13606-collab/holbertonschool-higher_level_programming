#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    say = 0
    for i in my_list:
        try:
            print("{:d}".format(i), end="")
            say += 1
        except (IndexError, ValueError, TypeError):
            pass
        if say == x:
            break
    print()
    return say
