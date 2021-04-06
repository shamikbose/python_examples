#!/bin/python

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    dict_valueCount = defaultdict(int)
    output = []
    flag = 0
    for line in queries:
        # print line
        if line[0] == 1:
            dict_valueCount[line[1]] += 1
        elif line[0] == 2:
            if dict_valueCount[line[1]] != 0:
                dict_valueCount[line[1]] -= 1
            if dict_valueCount[line[1]] == 0:
                del dict_valueCount[line[1]]
        else:
            for key in dict_valueCount.keys():
                if dict_valueCount[key] == line[1]:
                    flag = 1
                    break
            if flag == 1:
                output.append(1)
                flag = 0
            else:
                output.append(0)
        # print dict_valueCount
    return output


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input().strip())

    queries = []

    for _ in xrange(q):
        queries.append(map(int, raw_input().rstrip().split()))

    ans = freqQuery(queries)

    print "\n", ans
    print "\n"

    # fptr.close()
