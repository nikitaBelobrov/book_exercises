#!/usr/bin/env python3

shoplist = ['apples', 'mango', 'carrot', 'bananas']
name = 'swaroop'

# Index operation
print('Element 0 -', shoplist[0])
print('Element 1 -', shoplist[1])
print('Element 2 -', shoplist[2])
print('Element 3 -', shoplist[3])
print('Element -1 -', shoplist[-1])
print('Element -2 -', shoplist[-2])
print('Symbol 0 -', name[0])

# Slice of list
print('Elements from 1 to 3:', shoplist[1:3])
print('Elements from 2 to end:', shoplist[2:])
print('Elements from 1 to -1:', shoplist[1:-1])
print('Elements from begin to end:', shoplist[:])

# Slice of string
print('Symbols from 1 to 3:', name[1:3])
print('Symbols from 2 to end:', name[2:])
print('Symbols from 1 to -1:', name[1:-1])
print('Symbols from begin to end:', name[:])
