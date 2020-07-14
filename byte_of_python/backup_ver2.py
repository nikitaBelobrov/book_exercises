#!/usr/bin/env python3

import os
import time

source = [
    '/Users/nikita/Downloads/1.txt',
    '/Users/nikita/Downloads/2.txt'
]

target_dir = '/Users/nikita/Downloads/Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print('Folder created succesfully', today)

target = today + os.sep + now + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Backup creating succesfully. Output:', target)
else:
    print('Backup creating FAILED.')
