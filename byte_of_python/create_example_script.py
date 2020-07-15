#!/usr/bin/env python3
import os


def main():
    while True:
        filename = input('Input name of script: ').replace(' ', '_') + '.py'

        if os.path.exists(filename):
            print('File already exists.\n')
            continue
        break

    with open(filename, 'w') as f:
        f.write('#!/usr/bin/env python3\n')

    if os.system('chmod a+x ' + filename) == 0:
        print('File created successfully.')


if __name__ == '__main__':
    main()
