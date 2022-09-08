#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    n = len(arr)
    count = [0,0,0,0,0]
    count[0] = arr.count(1)
    count[1] = arr.count(2)
    count[2] = arr.count(3)
    count[3] = arr.count(4)
    count[4] = arr.count(5)
    biggest = max(count)
    bird_id = count.index(biggest) + 1
   
    return bird_id
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
