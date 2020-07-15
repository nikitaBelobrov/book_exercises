#!/usr/bin/env python3

def reverse(text):
    return text[::-1]


def is_palindrome(text):
    clear_text = text.lower()

    forbidden_symbols = (
        '.', ',', '!', '?', ':', ';', '-', '(', ')', '\n', ' ', '"', '\''
    )
    for symbol in forbidden_symbols:
        clear_text = clear_text.replace(symbol, '')

    return clear_text == reverse(clear_text)


something = input('Input text: ')
if (is_palindrome(something)):
    print('Yes, the text is palindrome')
else:
    print('No, the text is not palindrome')
