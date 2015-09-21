__author__ = 'sridhar'

arr = [1, 2, 2, 1, 3, 4, 3]


def getOdd(arr):
    if arr.__len__() == 0:
        return 0
    else:
        return reduce( lambda x, y: x ^ y, arr)

    print getOdd(arr1)
