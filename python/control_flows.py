#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

# IF

var = None
if var is True:
    pass
elif var is not True:
    pass
elif var in [True, False]:
    pass
elif var not in [True, False]:
    pass
elif var == 'something':
    pass
else:
    pass


# FOR

for word in ['this', 'is', 'a', 'sentence']:
    print(word)

    if word == 'a':
        # continues with the next iteration
        continue


# RANGE
range(10)

for i in range(0, 10, 3):
    print(i)

    # breaks out of the smallest enclosing for
    break


# Notes

# To change a sequence you are iterating over while inside the loop
# (for example to duplicate certain items), it is recommended that you first
# make a copy.
# Looping over a sequence does not implicitly make a copy.
# The slice notation makes this especially convenient:

# >>>
# >>> words = ['cat', 'window', 'defenestrate']
# >>> for w in words[:]:  # Loop over a slice copy of the entire list.
# ...     if len(w) > 6:
# ...         words.insert(0, w)
# ...
# >>> words
# ['defenestrate', 'cat', 'window', 'defenestrate']



