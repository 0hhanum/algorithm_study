# TRY 1
from itertools import combinations


def minimumAbsoluteDifference(arr):
    # Write your code here
    pairs = list(combinations(arr, 2))
    minimum = abs(pairs[0][0] - pairs[0][1])
    for i in pairs:
        value = abs(i[0] - i[1])
        if value < minimum:
            minimum = value
    return minimum


# TRY 2

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    minimum = arr[1] - arr[0]
    for i, a in enumerate(arr[:-1]):
        value = arr[i + 1] - a
        if value < minimum:
            minimum = value
    return minimum
