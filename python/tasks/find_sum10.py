#!/usr/bin/python3.4
import random


def random_int_array():
    return [random.randint(-100, 100) for i in range(50)]

if __name__ == "__main__":
    """
    Find pairs in an integer array whose sum is equal to 10
    (bonus: do it in linear time).
    """

    array = random_int_array()
    print("---- Quadratic ----")
    # print(array)

    # O(n)*O(n) = O(n^2)
    # Quadratic
    # O(n)
    for y in array:
        v = - y + 10

        # O(n)
        if v in array:
            print(y, v)

    print("---- Loglinear ----")
    # O(n log n)
    # loglinear
    sarray = sorted(array)

    def bin_search(array, find):
        middle = int(len(array) / 2)
        res = array[middle]
        if res == find:
            return True

        if len(array) == 1:
            return False

        if res < find:
            return bin_search(array[middle:], find)
        else:
            return bin_search(array[:middle], find)

    for x in sarray:
        if bin_search(sarray, - x + 10):
            print(x, - x + 10)


    print("---- Linear ----")
    # O(n) linear
    #
    # The best way would be to insert every element into a hash table
    # (without sorting). This takes O(n) as constant time insertion.
    # Then for every x, we can just look up its complement, T-x, which is O(1).
    # Overall the run time of this approach is O(n).

    hasht = {}
    # O(n)
    hasht = set(array)
    for h in hasht:
        # O(1)
        if - h + 10 in hasht:
            print(h, -h + 10)
