#!/usr/bin/env python3

class ShortInputException(Exception):
    '''User class of exception'''

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Input something: ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('Why you did EOF ?')
except ShortInputException as ex:
    print('ShortInputException: Length of inputed string -- {0}; ' +
          'expected minimum {1}.'.format(ex.length, ex.atleast))
else:
    print('Nothing exception.')
