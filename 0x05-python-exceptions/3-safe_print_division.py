#!/usr/bin/python3

def safe_print_division(a, b):
    """Function that divides two integers and orint the result."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
