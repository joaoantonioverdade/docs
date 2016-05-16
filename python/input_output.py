#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

# input
s = input('--> ')
print(s)

# fancy and common output printing
for x in range(1, 11):
    print(repr(x).zfill(3).rjust(3), end='->')
    print(str(x*x).zfill(3).rjust(3))

# print oneliner
for x in range(10):
    print(x, end='')

# open file
# r: read
# w: write
# a: appending (added to the end of file)
# r+: read and write
# default: r
# b: appended to one of the previous modes to open in binary mode
file_object = open('README.md', 'r')

# line endings automatically converted to \n
# \n      Unix
# \r\n    Windows

# methods
# .read(file_object.size)
file_object.read()

# if the end of file has been reached
file_object.read() == ''

# line by line
file_object.readline()

# memory efficient
for line in file_object:
    print(line, end='')

list_lines = list(file_object)
list_lines = file_object.readlines()

# write
if False:
    file_object.write('Sample line to write\n')

# close up
file_object.close()

# good practice (automatically closes file)
with open('README.md', 'r') as file_object:
    read_data = file_object.readline()
    # read_data = file_object.read()

# use json for interoperability
# reference http://json.org/
# serializing (Python hierarchies and convert them to string rep.)
import json
json_var = json.dumps([1, 'simple', 'list'])

# save to file
# json.dump(json_var, file_object)
# read from file
# obj = json.load(file_object)

# for specific Python serialization see pickle
