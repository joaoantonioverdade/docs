#!/usr/bin/python3.4

if __name__ == "__main__":
    """Given 2 integer arrays, determine if the 2nd array is a rotated version
     of the 1st array. Ex. Original Array A={1,2,3,5,6,7,8}
     Rotated Array B={5,6,7,8,1,2,3}
     Assume there are no duplicated numbers in the array"""

    A = [1, 2, 3, 4, 5, 6, 7, 8]
    B = [8, 1, 2, 3, 4, 5, 6, 7]
    B = [5, 6, 7, 8, 1, 2, 3, 4]

    print(A, B)

    index_A = 0
    index_X = 0

    # find pivot of A in B
    for idx, x in enumerate(B):
        if x == A[0]:
            pivot = idx
            break

    if A == B[pivot:] + B[:pivot]:
        print("2nd array is a rotated version if the 1st array")
