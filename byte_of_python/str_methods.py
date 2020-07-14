#!/usr/bin/env python3

name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, string starts with "Swa"')

if 'a' in name:
    print('Yes, name includes symbol "a"')

if name.find('war') != -1:
    print('Yes, name includes "war"')

delimiter = '_*_'

mylist = ['Brasil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
