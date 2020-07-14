#!/usr/bin/env python3

# Simple assignment
shoplist = ['apples', 'mango', 'carrot', 'bananas']
mylist = shoplist  # mylist is another name of same object

del shoplist[0]

print('shoplist:', shoplist)
print('mylist:', mylist)

# Copying by full slice
mylist = shoplist[:]
del mylist[0]

print('\nshoplist:', shoplist)
print('mylist:', mylist)
