#!/usr/bin/env python3
import time

try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2)
except KeyboardInterrupt:
    print('!! You canceled reading.')
finally:
    f.close()
    print('(Clearing: Closing of file)')