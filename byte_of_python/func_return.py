#!/usr/bin/env python3

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Numbers are equal'
    else:
        return y


print(maximum(2, 3))
