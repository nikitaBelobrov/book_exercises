#!/usr/bin/env python3

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print('Adress of Swaroop:', ab['Swaroop'])

# Deleting of key-value pair
del ab['Spammer']


print('\nIn address book {0} contacts\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {0} have address {1}'.format(name, address))

# Adding key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print('Address of Guido:', ab['Guido'])
