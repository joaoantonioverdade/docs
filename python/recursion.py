#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

# The three laws of recursion
# 1. A recursive algorithm must have a **base case**
# 2. A recursive algorithm must change its state and move toward the base case
# 3. A recursive algorithm must call itself, recursively


def list_sum(numList):

    if len(numList) > 1:
        first_last = numList.pop()
        second_last = numList.pop()

        numList.append(first_last + second_last)
        return list_sum(numList)
    else:
        return numList[0]


def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])


def toStr(n):
    if n < 10:
        return str(n)
    else:
        return str(n // 10) + toStr(n % 10)

if __name__ == "__main__":
    nList = [1, 3, 5, 7, 9]

    print(sum(nList))
    print(list_sum(nList))
    print(listsum(nList))

    print()

    print(list(toStr(5)))
    print(list(toStr(25)))
    print(list(toStr(225)))
    print(list(toStr(2455)))
