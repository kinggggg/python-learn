#!/usr/bin/python
#Filename: class_init.py

class Person:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print self.name

p = Person("tom")
p.sayHi()
