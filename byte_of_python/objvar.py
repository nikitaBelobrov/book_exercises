#!/usr/bin/env python3

class Robot:
    '''Represents robot with name'''
    # Count of robots
    population = 0

    def __init__(self, name):
        '''Initializing of data'''
        self.name = name
        print('Initializing {0}'.format(self.name))

        # Adding new robot to population
        Robot.population += 1

    def __del__(self):
        '''I am dying'''
        print('{0} destroyed'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} was last robot.'.format(self.name))
        else:
            print('{0} working robots left.'.format(Robot.population))

    def say_hi(self):
        '''Robot greeting'''
        print('Hello! My owners named me {0}'.format(self.name))

    def how_many():
        '''Prints count of robots'''
        print('We have {0:d} robots.'.format(Robot.population))

    how_many = staticmethod(how_many)


droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.how_many()

print('\nNow robots do some work...\n')

print('Robots finish its work. Let\'s delete them.')
del droid1
del droid2

Robot.how_many()
