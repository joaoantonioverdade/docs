#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------

# Data Structures
# reference:
# https://docs.python.org/3/tutorial/datastructures.html

# Lists
square = []
# .append(value)
# .insert(idx,value)
# .extend(L)
# .remove(value)
# .pop([index])
# .clear()
# .index(value)
# .count(value)
# .sort()
# .reverse()
# .copy()
#
# notes:
# remove(value),index(value) -> only the first found element
# to implement queues is better to use: collections.deque
#
# reverse order: list[::-1]

# List comprehensions
#
squares = [x*x for x in range(10)]
squares = list(map(lambda x: x**2, range(10)))  # not so readable

matrix_no_identity = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
apply_function = [abs(x) for x in [-2, -1, 0, 1, 2]]
call_method = [x.sort() for x in [squares, matrix_no_identity]]
create_tuple = [(x, x*x) for x in range(10)]

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flaten_list = [num for elem in vec for num in elem]  # [1,2,3,4,5,6,7,8,9]

# Del statement
del squares[0]
del squares[1:-1]
del squares

# Tuples and sequences
# A tuple is a IMMUTABLE number of values separated by commas
# the output of a tuple is always enclosed in parentheses so that nested
# tuples are interpreted correctly
#
t = 123, 456, 'hello!'
# t[0] 	# 123
# t 	# (123, 456, 'hello!')
#
# unpack:
first_number, second_number, first_string = t
#
# notes:
# one tuple element is instantiated as:
# t = 1,

# Sets
# UNORDERED collection with NO DUPLICATE elements
# set([L])
# .add(elem)
# .remove(elem)
# .discard(elem)
# .pop()
# .clear()
new_set = {}
new_set = set([1, 1, 2, 3])  # {1, 2, 3} removes duplicates
#
a = set('abracadabra')
b = set('alacazam')
# a , b unique in a and b = {'c', 'd', 'r', 'b', 'a'} {'c', 'z', 'm', 'l', 'a'}
# a - b in a but not in b      = {'d', 'r', 'b'}
# a | b either a or b          = {'z', 'l', 'c', 'd', 'r', 'b', 'm', 'a'}
# a & b in both a and b        = {'c', 'a'}
# a ^ b in a or b but not both = {'z', 'l', 'd', 'r', 'b', 'm'}
#

# Dictionaries (Hash Tables)
# Indexed by immutable keys (string or numbers,tuples*)
# UNORDERED set of key: value pairs with UNIQUE KEYS
#
dictionary = {}
dictionary = {'key1': 9999, 'key2': 1111}
dictionary = {('key1', 9999), ('key2', 1111)}
dictionary = dict(key1=9999, key2=1111)
#
dictionary.keys()                       # existing keys
del dictionary['key2']                  # deletes key
'key2' in dictionary                    # key is in dictionary
#
dictionary["key3"] = "can be a string"  # adds key

for key, value in dictionary.items():
    pass
    # print(key, value)

for value in dictionary.values():
    pass
    # print(value)

# The only dictionary operations that are not O(1)
# are those that require iteration.

# Linear data structures
#
# Once an item is added, it stays in that position relative to the other
# elements that came before and came after it.
#
# Stack (LIFO last-in first-out)
# common list..
#
# Queue (FIFO first-in first-out)
# import queue
# q = queue.Queue()
#
# Deque (double-ended queue)
# import collections
# d = collections.deque()
# d.append("b")
# d.appendleft("a")
# d.append("c")
