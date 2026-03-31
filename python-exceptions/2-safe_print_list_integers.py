#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    say = 0

    for i in range(x):

        try:
            print("{:d}".format(my_list[i]), end="")
            say += 1
        except (TypeError, ValueError):
            pass
        except IndexError:
            break
    print()
    print(say)
