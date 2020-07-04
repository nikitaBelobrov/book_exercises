#!/usr/bin/env python3

def print_max(a, b):
    '''Print maximum from two numbers.

    Both numbers must be integers.'''

    x = int(a)  # convert number to integer, if possible
    y = int(b)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


print_max(3, 5)
print(print_max.__doc__)
