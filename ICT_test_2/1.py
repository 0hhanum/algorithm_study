#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'balancedSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSum(arr, n):
    # Write your code here
    l_index = 0
    r_index = -1
    L = arr[l_index]
    R = arr[r_index]
    while L != R or (r_index + n - 1) - l_index > 2:
        if L <= R:
            l_index += 1
            L += arr[l_index]
        elif L > R:
            r_index -= 1
            R += arr[r_index]
    return l_index + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = balancedSum(arr, arr_count)

    fptr.write(str(result) + '\n')

    fptr.close()
