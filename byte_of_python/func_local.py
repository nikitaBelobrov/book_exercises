#!/usr/bin/env python3

x = 50


def func(x):
    print('x = ', x)
    x = 2
    print('local x changed on', x)


func(x)
print('x is still', x)
