#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
    except:
        result =  None
    finally:
        print("section preceded by Inside result:{} / {} = {}".format(a, b, result))
