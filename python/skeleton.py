#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

# Style guide: https://www.python.org/dev/peps/pep-0008/

# CamelCase for classes
# lower_case_with_underscores for functions and methods

# wrap lines so they don't exceed 79 characters
# -----------------------------------------------------------------------------


def definition(optional=True):
    """Docstrings, first line always short, concise summary of object purpose.

    Start with capital letter, finish with period.
    Second line always blank.
    """
    print(definition.__doc__)
    pass


def accumulator(value, L=[]):
    """Accumulator(1) ... accumulator(2) ... -> L = [1,2]."""
    L.append(value)
    return L


def arbitrary_arguments(separator="#", *args):
    """Args wrapped up in a tuple."""
    return separator.join(args)


def unpacking(first="optional", second="optional"):
    """List or tuple unpacking."""
    args = [3, 6]
    print(list(range(*args)))

    args = {"first": "primeiro",
            "second": "segundo"}

    print(args)
    # print(*args)
    # unpacking(**args)

    # *var_name  -> dinamic number of arguments might be passed to function
    # **var_name -> dinamic number of named arguments


def incrementor(value):
    """Syntactic sugar use of lambda.

        function = incrementor(1)
        print(function(1))
        print(function(99))

        lambda, anonymous (unbound) function
    """
    return lambda sugar: sugar + value


# def function_annotation() -> "This is the annotation":
#     print("Annotations:", function_annotation.__annotations__)


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # priv

if __name__ == "__main__":
    import sys
    print(sys.argv[0])
