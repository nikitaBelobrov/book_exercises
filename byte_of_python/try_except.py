#!/usr/bin/env python3

try:
    text = input('Input something: ')
except EOFError:
    print('\nWhy you did EOF ?')
except KeyboardInterrupt:
    print('\nYou canceled operation')
else:
    print('You inputed {0}.'.format(text))
