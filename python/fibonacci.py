#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

# fibonacci, sequence of numbers starting with 0 and 1,
# where the subsequent number is the sum of the two previous numbers


def fib(length):
    fibonacci = [0, 1]

    for i in range(length):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return fibonacci
