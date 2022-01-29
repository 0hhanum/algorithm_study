#!/bin/python3

import os


#
# Complete the 'chooseFlask' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY requirements
#  2. INTEGER flaskTypes
#  3. 2D_INTEGER_ARRAY markings
#

def chooseFlask(requirements, flaskTypes, markings):
    # Write your code here
    requirements.sort()
    maximum = requirements[-1]

    table = {}
    nums = []
    for flask, capacity in markings:
        if flask not in table:
            table[flask] = [capacity, ]
            nums.append(1)
        else:
            table[flask].append(capacity)
            nums[flask] += 1

    minValue = float('inf')
    result = -1
    r_length = len(requirements)

    for idx, capacities in enumerate(table.values()):
        # capacities = list(set(capacities))
        # capacities.sort()
        if capacities[-1] < maximum:
            continue
        length = nums[idx]
        index = r_index = 0
        waste = -1
        while r_index < r_length and index < length:
            c = capacities[index]
            target = requirements[r_index]
            if c >= target:
                waste += c - target
                r_index += 1
                continue
            else:
                index += 1

        if waste < minValue and waste != -1:
            minValue = waste
            result = idx
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    requirements_count = int(input().strip())

    requirements = []

    for _ in range(requirements_count):
        requirements_item = int(input().strip())
        requirements.append(requirements_item)

    flaskTypes = int(input().strip())

    markings_rows = int(input().strip())
    markings_columns = int(input().strip())

    markings = []

    for _ in range(markings_rows):
        markings.append(list(map(int, input().rstrip().split())))

    result = chooseFlask(requirements, flaskTypes, markings)

    fptr.write(str(result) + '\n')

    fptr.close()
