#!/usr/bin/python
#Filename: objvar.py

class Person:
    '''Represents a person'''

    population = 0

    def __init__(self, name):
        self.name = name
        print '(Init %s)' % self.name

        Person.population += 1

    def __del__(self):
        '''I am dying.'''
        print '%s says bye.' % self.name

        Person.population -= 1

        if Person.population == 0:
            print "i am the last one."
        else:
            print 'There are still %d people left' % Person.population

    def sayHi(self):
        '''sayHi method'''
        print 'my name is %s' % self.name

    def howMany(self):
        if Person.population == 1:
            print 'i am the only one person'
        else:
            print 'we have %d persons left' % Person.population

one = Person('one')
one.sayHi();
one.howMany()

two = Person('two')
two.sayHi()
two.howMany()

print Person.__doc__
print Person.sayHi.__doc__
