#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
"""
prints the first x elements of a list and only integers

Args:
    x: number of elements to access
    Return: the real number of integers printed
"""
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            count += 1

    print()
    return (count)
