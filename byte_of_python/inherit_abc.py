#!/usr/bin/env python3
from abc import *


class SchoolMember(metaclass=ABCMeta):
    '''Represents any member in school'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Created SchoolMember: {0})'.format(self.name))

    @abstractmethod
    def tell(self):
        '''Print member information'''
        print('Name: "{0}" Age: "{1}"'.format(self.name, self.age), end=' ')


class Teacher(SchoolMember):
    '''Represents a teacher'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Created Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {0:d}'.format(self.salary))


class Student(SchoolMember):
    '''Represents a student'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Created Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {0:d}'.format(self.marks))


t = Teacher('Mrs. Shrividia', 40, 30_000)
s = Student('Swaroop', 25, 75)

print()

members = [t, s]
for member in members:
    member.tell()
