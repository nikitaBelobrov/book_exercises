#!/usr/bin/env python3

def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input('Input text: ')
if (is_palindrome(something)):
    print('Yes, the text is palindrome')
else:
    print('No, the text is not palindrome')
