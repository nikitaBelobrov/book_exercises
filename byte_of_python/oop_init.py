#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello! My name is', self.name)


p = Person('Nikita')
p.say_hi()
