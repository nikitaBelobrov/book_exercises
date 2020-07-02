#!/usr/bin/env python3

def print_max(a, b):
    if a > b:
        print(a, 'is max')
    elif a == b:
        print(a, 'is equal', b)
    else:
        print(b, 'is max')


print_max(3, 9)

x = 5
y = 5

print_max(x, y)
