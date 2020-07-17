#!/usr/bin/env python3
'''
Реализуйте команду replace. Эта команда заменяет одну строку другой в списке
переданных ей файлов.
'''
import os


def replace(text, new_text, filelist):
    '''Replaces one text to new text in all files'''
    for file in filelist:
        if not os.path.exists(file) or not os.path.isfile(file):
            continue
        with open(file) as f:
            current_text = f.read()
        with open(file, 'w') as f:
            f.write(current_text.replace(text, new_text))
        print('Text replaced succesfully!')


def main():
    files = ('../poem.txt', '1.txt', '2.txt', '132')
    text = input('Input text to replace: ')
    new_text = input('Input new text: ')

    replace(text, new_text, files[:])


if __name__ == '__main__':
    main()
