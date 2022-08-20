#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    l = len(s)
    mistakes = 0
    for m in range(0, l, 3):
        if s[m] != 'S':
            mistakes += 1
        if s[m+1] != 'O':
            mistakes += 1
        if s[m+2] != 'S':
            mistakes += 1
    return mistakes
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
