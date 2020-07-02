#!/usr/bin/env python3

while True:
    s = input('Input something: ')
    if s == 'exit':
        break
    if len(s) < 3:
        print('Too short text.')
        continue
    print('Text has normal length.')
