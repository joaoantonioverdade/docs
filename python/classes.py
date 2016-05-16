#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

# Standard features of Object Oriented Programming

# NAMESPACE, mapping from names to objects, ex. abs()
# z.real, real is an ATTRIBUTE of object z
# attributes may be read-only or writable
# writable attributes can be deleted: del z.real


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)  # test spam
    do_nonlocal()
    print("After nonlocal assignment:", spam)  # nonlocal spam
    do_global()
    print("After global assignment:", spam)  # nonlocal spam

scope_test()
print("In global scope:", spam)  # global spam


# Class definition
class ClassName:
    """
    A class supports two operations: attribute references and instantiation.
    """
    var = 12345     # shared by all instances until new assignment
    var_list = []   # shared by all instances

    def funct(self):
        print("funnnnn")
        return 'string'

    def __init__(self, value1=0):
        self.var1 = value1      # unique variables to each instance
        self.unshare_list = []

# attribute reference
ClassName.var       # OK
ClassName.funct     # OK

# class instantiation
my_new_class = ClassName(99)
my_new_class2 = ClassName()

print(my_new_class.var1)

# instance objects
# valid attribute names: data attributes and methods
# the attributes can be assigned and even deleted
my_new_class.counter = 2
del my_new_class.counter

ClassName.funct(my_new_class)   # function
my_new_class.funct()            # method

# store reference to function
stored_method = my_new_class.funct
stored_method()

# assigning unshares variables due to ref another object?
my_new_class.var = 1234
print(my_new_class.var)
print(my_new_class2.var)

my_new_class.var_list.append("first")
my_new_class2.var_list.append("second")

# shared variables
print(my_new_class.var_list)
print(my_new_class2.var_list)

# unshare list
my_new_class.unshare_list.append("first")
my_new_class2.unshare_list.append("second")

print(my_new_class.unshare_list)
print(my_new_class2.unshare_list)

# random remarks
# data attributes override method attributes with the same name
# possible conventions include capitalizing method names, prefixing
# data attribute names with a small unique string
# (perhaps just an underscore)


class Bag:
    # methods may call other methods
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def add_Twice(self, x):
        self.add(x)
        self.add(x)


# inheritance
class DerivedClassName(ClassName):
    var_second = 54321

# Derived classes may override methods of their base classes.
# An overriding method in a derived class may in fact want to
# extend rather than simply replace the base class method of the same name.
# call BaseClassName.methodname(self,arguments)

# isinstance()
# issubclass()

# private variables
# there aren't none
# convention uses a prefixed underscore (ex. _spam)
# name mangling is helpful for letting subclasses override methods without
# breaking intraclass method calls


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


# convention for the Pascal "record" or the C "struct"
class Employee:
    pass

john = Employee()
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

# iterators
#
# This style of access is clear, concise, and convenient.
# The use of iterators pervades and unifies Python.
# Behind the scenes, the for statement calls iter() on the container object.
# The function returns an iterator object that defines the method __next__()
# which accesses elements in the container one at a time. When there are no
# more elements, __next__() raises a StopIteration exception which tells the
# for loop to terminate. You can call the __next__() method using the next()
# built-in function;

string = 'abc'
iterator = iter(string)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))


# creating a iterator behavior
class Tokenizer:
    def __init__(self, data):
        self.data = data
        self.index = data.count(' ') + 1
        print("index " + str(self.index))

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index = self.index - 1
        self.first_token = self.data[:self.data.find(' ')]
        self.data = self.data[self.data.find(' ') + 1:]
        return self.first_token

# calling the new iterator
tok = Tokenizer('Uma frase simples para ser tokenizada ')
for token in tok:
    print(token)

# Generators are a simple and powerful tool for creating iterators.
# They are written like regular functions but use the yield statement whenever
# they want to return data. Each time next() is called on it, the generator
# resumes where it left off (it remembers all the data values and which
# statement was last executed)


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

print([char for char in reverse('golf')])


# generator expressions

soma = sum(i*i for i in range(10))
print(soma)

xvec = [10, 20, 30]
yvec = [7, 5, 3]
soma = sum(x*y for x, y in zip(xvec, yvec))

print(max([1, 2, 4, 5, 3, 6, 99, 2, 2, 1, 1]))
