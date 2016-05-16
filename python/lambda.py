#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# references:
# http://www.blog.pythonlibrary.org/2010/07/19/the-python-lambda/
# https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/

# lambda is an anonymous (unbound) function
# used for building function objects (as def)

import math


def sqroot(x): return math.sqrt(x)
print(sqroot(9))

# square_rt = lambda x: math.sqrt(x)
# print(square_rt(9))

def sum(x, y): return x + y
# sum = lambda x,y: x + y
# out = lambda *x: print(' '.join(map(str, x)))

# When to use?
# Situations we need a simple one-off function, one use only.
# When to use a short anonymous function?
# Callbacks (gui frameworks), mathematical/string operations
# functions, conditional expressions,

# lambda : print("true") if condition() else print("false")
# lambda x: 'miríade' if x > 10000 else 'caterva'

# confusing because:
# does't have a return implicit
# lacks other language lambda power
# introduced has a anonymous function but generaly used has procedure
#
# The legitimate use case for lambda is where you want to use a function
# without assigning it, e.g:
# sorted(players, key=lambda player: player.rank)

# Guido overview of the matter:
# http://www.artima.com/weblogs/viewpost.jsp?thread=147358
