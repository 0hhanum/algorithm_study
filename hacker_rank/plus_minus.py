#!/bin/python3


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    result = [0, 0, 0]  # neg, zero, pos

    for i in arr:
        if i < 0:
            result[0] += 1
        elif i > 0:
            result[2] += 1
        else:
            result[1] += 1
    print(result[2] / sum(result))
    print(result[0] / sum(result))
    print(result[1] / sum(result))


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
