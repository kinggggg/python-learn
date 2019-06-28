#!/usr/bin/python
#Filename: inherit.py

class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print 'Name: %s, Age: %s' %(self.name, self.age)

class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: %s' % self.salary


t = Teacher('tom', 30, 100)
t.tell();