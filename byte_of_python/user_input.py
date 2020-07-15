#!/usr/bin/env python3

def reverse(text):
    return text[::-1]


def is_palindrome(text):
    clear_text = text.lower()\
                     .replace(',', '')\
                     .replace('.', '')\
                     .replace(' ', '')
    return clear_text == reverse(clear_text)


something = input('Input text: ')
if (is_palindrome(something)):
    print('Yes, the text is palindrome')
else:
    print('No, the text is not palindrome')
