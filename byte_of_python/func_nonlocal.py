#!/usr/bin/env python3

def func_outer():
    x = 2
    print('x =', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('Local x changed to', x)


func_outer()
