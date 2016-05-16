#!/usr/bin/python3.4

"""
A wrapper...

Convert the interface of a class into another interface clients expect.
Adapter lets classes work together that could not otherwise because of
incompatible interfaces

Wrap an existing class with a new interface

source:
http://python-3-patterns-idioms-test.readthedocs.org/en/latest/ChangeInterface.html
"""

import datetime


class oldClass:
    def first_method(self):
        print("The time is ")

    def second_method(self):
        print(datetime.datetime.now().time())


class newClass:
    def get_time(self):
        pass


class adapter(newClass):
    def __init__(self, oldClass):
        self.oldClass = oldClass

    def get_time(self):
        self.oldClass.first_method()
        self.oldClass.second_method()


# testing
old = oldClass()
adapt = adapter(old)
adapt.get_time()
