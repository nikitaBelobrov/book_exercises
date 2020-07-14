#!/usr/bin/env python3

import os
import time
import zipfile

source = [
    '/Users/nikita/Downloads/1.txt',
    '/Users/nikita/Downloads/2.txt'
]

target_dir = '/Users/nikita/Downloads/Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)


today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('Input your comment --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'


if not os.path.exists(today):
    os.mkdir(today)
    print('Folder created succesfully', today)

for file in source:
    with zipfile.ZipFile(target, 'a') as myzip:
        myzip.write(file)

print('Backup creating succesfully. Output:', target)
