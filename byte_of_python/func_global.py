#!/usr/bin/env python3

x = 50


def func():
    global x

    print('x =', x)
    x = 2
    print('global x changed to', x)


func()
print('Value of x is', x)
