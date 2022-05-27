#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'textQueries' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY sentences
#  2. STRING_ARRAY queries
#
from collections import defaultdict


def textQueries(sentences, queries):
    # Write your code here
    answer = [[-1] for _ in queries]
    table = defaultdict(set)
    for idx, sentence in enumerate(sentences):
        for word in sentence.split(" "):
            table[word].add(idx)

    for q_idx, query in enumerate(queries):
        tmp = set()
        for i, word in enumerate(query.split(" ")):
            if i == 0:
                tmp = table[word]
            else:
                tmp = tmp & table[word]
            if not tmp:
                break
        if tmp:
            answer[q_idx] = sorted(list(tmp))

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentences_count = int(input().strip())

    sentences = []

    for _ in range(sentences_count):
        sentences_item = input()
        sentences.append(sentences_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    result = textQueries(sentences, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
