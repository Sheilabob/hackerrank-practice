#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    a.sort()
    b.sort()
    biggest = b[0]
    holding_pen = []
    for i in range (biggest):
        holding_pen.append(i+1)
    for i in range (biggest):
        for j in range (n):
            if (i+1)%a[j] != 0:
                if (i+1) in holding_pen:
                    holding_pen.remove(i+1)
    holding_pen_two = []
    o = len(holding_pen)
    for i in range (o):
        holding_pen_two.append(holding_pen[i])
    for i in range (o):
        for j in range (m):
            if b[j]%holding_pen[i] != 0:
                if holding_pen[i] in holding_pen_two:
                    holding_pen_two.remove(holding_pen[i])
    return len(holding_pen_two)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
