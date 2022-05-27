#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numberOfWays' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY queries as parameter.
#

def numberOfWays(queries):
    # Write your code here
    answer = []
    for a, b in queries:
        tmp = 0
        minimum = min(a, b)
        for i in range(minimum):
            tmp += (a - i) * (b - i)
        answer.append(tmp)
    return answer
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    result = numberOfWays(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
