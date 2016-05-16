#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

# Packages
#
# Structure for python's modules namespace
# ex. package.module_A
# when importing a package Python searches through directories on sys.path
# __init__.py are required to treat the directories as containing packages

# the __init__.py can define a list named __all__ of all the module names
# it provides has an example_
# __all__ =["echo","surround","reverse"]
#
import package_example.block.example

import fibonacci
# from fibonacci import fib

from fibonacci import *
# import all names except those beginning with an underscore (_), frowned upon

package_example.block.example.block_func()

print(fibonacci.__name__)
print(fibonacci.fib(10))
print(fib(10))

# when running a Python module as: python fibonnaci.py <arguments>
# the code in the module will be executed as if imported with the
# __name__ set to "__main__", not called when just imported

if __name__ == "__main__":
    import sys
    # fibonacci.fib(int(sys.argv[1]))

# returns which names a module defines
print(dir(fibonacci))
print(dir(sys))

# currently defined
print(dir())
