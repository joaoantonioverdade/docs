#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

# Operating System Interface
import os
os.getcwd()
os.chdir('/usr/bin/')
print(os.system('ls'))
print(dir(os))
print(help(os))

# daily file and directory management tasks:
import shutil
shutil.copyfile('original.file', 'destination.file')
print(dir(shutil))

# file wildcards
import glob
print(glob.glob('*.py'))

# command line arguments
# simple: sys.argv
# getopt(): as Unix conventions
# argparse: powerful and flexible

# string pattern matching
# import re

# math operations
# import math

# internet access
# data from urls: urllib.request
# email: smtplib

from urllib.request import urlopen
for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    if 'EST' in line or 'EDT' in line:  # look for Eastern Time
        print(line)

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
                """To: jcaesar@example.org
                   From: soothsayer@example.org

                   Beware the Ides of March.
                   """)
server.quit()

# performance measurement
import timeit
t = timeit.Timer()
t('a=b;b=c;c=a', 'b=1;c=2').timeit()

# quality control
# One approach for developing high quality software is to write tests for
# each function as it is developed and to run those tests frequently during
# the development process.


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests

# more comprehensive set of tests see: unittest

# multi-threading
# import threading
# While those tools are powerful, minor design errors can result in problems
# that are difficult to reproduce. So, the preferred approach to task
# coordination is to concentrate all access to a resource in a single thread
# and then use the queue module to feed that thread with requests from other
# threads. Applications using Queue objects for inter-thread communication and
# coordination are easier to design, more readable, and more reliable.

# tools for working with lists
#
# import array -> only homogeneous data more compactly
#

import collections
d = collections.deque(["task1", "task2", "task3"])
d.append("task4")
d.popleft()

# faster appends and pops from the left side, slower lookups in the middle
# well suited fro queues and breadth first tree searches
