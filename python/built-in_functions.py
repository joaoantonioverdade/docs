#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

# https://docs.python.org/2/library/functions.html

# Absolute value
assert 10 == abs(-10)

# Return True if all elements of the iterable are true
assert all([2 == 1 + 1, True, 1])   #

# Return True if any element of the iterable is true
assert any([False, 0, True])

# Convert an integer number to a binary string
binary_string = [bin(n) for n in range(5)]
print(binary_string)

# Return the string representing a character whose Unicode code point is the
# integer i
string = [chr(n) for n in range(100, 103)]
print(string)

# Return an integer representing the Unicode code point of that character
string_integers = [ord(n) for n in 'def']
print(string_integers)

# Convert an integer number to a lowercase hexadecimal
print(hex(-42))

# Convert an integer number to an octal string
print(oct(-42))


# A class method receives the class as implicit first argument,
# just like an instance method receives the instance.
# @classmethod
# A static method does not receive an implicit first argument.
# @staticmethod

class Date(object):

    day = 0
    month = 0
    year = 0

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))

        new_date = cls(day, month, year)
        # cls = __init__(,day, month, year)

        return new_date

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 2016

today = Date(1, 1, 2001)
tomorrow = Date("02-01-2001")
date_valid = Date.is_date_valid("01-01-2016")

assert isinstance(today, Date)
assert isinstance(tomorrow, Date)
assert not isinstance(date_valid, Date)     # due to the staticmethod


# compile source into code
# modes: exec, sequence of statements
#        eval, single expression
#
# exec executes but returns None
# eval evaluate expression

codeobj = compile('x = 2\nprint(x)', '<string>', mode='exec')
eval(codeobj)

x = False
assert eval('not x')


# Delete a named attribute
# Assigns the value to the attribute
# Return the value of the named attribute
# Check if have an attribute

class x:
    pass

x.foobar = True

delattr(x, 'foobar')        # same as: del x.foobar
setattr(x, 'foobar', 123)   # same as x.foobar = 123
getattr(x, 'foobar')        # x.foobar
assert hasattr(x, 'foobar')

# take two numbers as arguments and return a pair of numbers consisting of
# their quotient and remainder when using the integer division
# for integers same as (a // b, a % b)
# for floats same as (q, a % b)
print(divmod(10, 6))

# returns an enumerate objet
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons, start=1)))


# functional approach
#
# filter(function, iterable)
# extracts each element in the sequence for which the function returns True
print(list(filter((lambda x: x < 0), range(-5, 5))))
#
# map(function, iterable,...)
# return an iterator that applies function to every item of iterable,
# yielding the results
sqr = list(map((lambda x: x*x), range(5)))
print(sqr)
#
# reduce
# passes the current value along with the next item from the list
from functools import reduce
print(reduce((lambda x, y: x + y), [1, 2, 4, 8, 16]))

# Convert a value to a formatted representation
# https://docs.python.org/3.5/library/string.html#formatspec

'{0}, {1}, {2}'.format('a', 'b', 'c')   # 'a, b, c'
'{}, {}, {}'.format('a', 'b', 'c')      # 'a, b, c'
'{2}, {1}, {0}'.format('a', 'b', 'c')   # 'c, b, a'
'{2}, {1}, {0}'.format(*'abc')          # 'c, b, a'
'{0}{1}{0}'.format('abra', 'cad')       # 'abracadabra'

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
'Coordinates: {latitude}, {longitude}'.format(**coord)

# return the length of an object
len(["obj1", "obj2"])

# return the largest item in an iterable
# return the smallest item in an iterable
# return the floating point value number rounded to ndigits
# return the sum of the items
assert max([-3, -2, -1, 0, 1])
assert min([1, 2, 3, 4, 5])
print(round(0.5))
print(round(-0.5))
print(round(1.5))
assert sum([2, -1])

# Return a property attribute


class C:
    def __init__(self):
        self._x = None

    # C.x
    # or @property
    def getx(self):
        return self._x

    # C.x = value
    # or @x.setter
    def setx(self, value):
        self._x = value

    # del C.x
    # or @x.deleter
    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

# return a reversed iterator
# return a new sorted list from the items in iterable
# make an iterator that aggregates elements from each of the iterables
print(list(reversed(range(5))))
print(list(sorted([3, 2, 1, 4, 6])))
print(zip([1, 2, 3], [4, 5, 6]))

# return the type of an object
x = 99,
print(type(x))
