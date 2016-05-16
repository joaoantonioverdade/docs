#!/usr/bin/python3.4

"""
Define a common API for a set of subclasses

Creates an instance of several families of classes.

Provide an interface for creating families of related or dependent
objects without specifying their concrete classes.

Example:
http://www.j4nu5.com/abstract-classes-and-factory-design-pattern-in-python.html
"""

# Abstract Base Classes
# http://docs.python.org/3.5/library/abc.html
import abc


class AbstractClass(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def hello(self, *args, **kwargs):
        pass


class PTConcrete(AbstractClass):

    language = ""

    def __init__(self, *args, **kwargs):
        self.language = "português"

    def hello(self, *args, **kwargs):
        print("olá")


class ENConcrete(AbstractClass):

    language = ""

    def __init__(self, *args, **kwargs):
        self.language = "inglês"

    def hello(self, *args, **kwargs):
        print("hello")


obj = ENConcrete()
obj2 = PTConcrete()

obj.hello()
obj2.hello()
