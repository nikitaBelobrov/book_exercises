#!/usr/bin/env python3

'''
Создайте собственную программу "Адресная книга", работающую из командной 
строки и позволяющую просматривать, добавлять, изменять, удалять или искать 
контактные данные ваших знакомых. Кроме того, эта информация также должна 
сохраняться на диске для последующего доступа.
'''
import pickle
import os


class AddressBook:
    '''Represents addressbook'''

    def __init__(self, filename):
        self.filename = filename
        self.contacts = {}

    def show_all_contacts(self):
        print()
        for name in self.contacts:
            print('{0}: {1}'.format(name, self.contacts[name].email))

    def add_new_contact(self):
        name = input('Input name: ')
        email = input('Input email: ')

        self.contacts[name] = ContactCard(name, email)
        print('Created new contact: {0}'.format(name))

    def find_contact(self):
        name = input('Input name: ')
        if name in self.contacts:
            print('{0}: {1}'.format(name, self.contacts[name].email))
        else:
            print('Contact "{0}" not found.'.format(name))

    def change_contact(self):
        name = input('Input name: ')
        new_email = input('Input new email: ')

        self.contacts[name].email = new_email

    def delete_contact(self):
        name = input('Input name: ')
        del self.contacts[name]
        print('Deleted contact: {0}'.format(name))


class ContactCard:
    '''Represents contact card in addressbook'''

    def __init__(self, name, email):
        self.name = name
        self.email = email


def main():
    filename = 'my_addressbook.data'

    if not os.path.exists(filename):
        my_addressbook = AddressBook(filename)
        with open(filename, 'wb') as f:
            pickle.dump(my_addressbook, f)
    else:
        with open(filename, 'rb') as f:
            my_addressbook = pickle.load(f)

    print(
        '1 - show all, \n2 - add new, \n3 - find contact, ' +
        '\n4 - change contact, \n5 - delete contact'
    )

    try:
        while True:
            command = input('\nInput command: ')

            if command == '1':
                my_addressbook.show_all_contacts()
            elif command == '2':
                my_addressbook.add_new_contact()
            elif command == '3':
                my_addressbook.find_contact()
            elif command == '4':
                my_addressbook.change_contact()
            elif command == '5':
                my_addressbook.delete_contact()
            elif command == 'quit':
                break
    finally:
        # Save all changes
        with open(filename, 'wb') as f:
            pickle.dump(my_addressbook, f)


if __name__ == '__main__':
    main()
