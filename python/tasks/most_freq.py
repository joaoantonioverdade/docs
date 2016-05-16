#!/usr/bin/python3.4
import random

def random_int_array():
    return [random.randint(0, 100) for i in range(50)]

if __name__ == "__main__":
    """
    Finds one of the most frequent integer in an array.
    """

    array = random_int_array()
    print(sorted(array))

    most_value = 0
    most_freq = 0
    for n in set(array):
        if array.count(n) > most_freq:
            most_freq = array.count(n)
            most_value = n

    print(most_value, most_freq)

    # or

    print(max(set(array), key=array.count))
