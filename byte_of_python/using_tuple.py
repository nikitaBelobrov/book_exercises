#!/usr/bin/env python3

zoo = ('python', 'elephant', 'penguin')
print('Count of animals is -', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Count cells in zoo -', len(new_zoo))
print('All animals in new zoo:', new_zoo)
print('Animals from old zoo:', new_zoo[2])
print('Last animal from old zoo:', new_zoo[2][-1])
print('Count of animals in new zoo -', len(new_zoo) - 1 + len(new_zoo[2]))
