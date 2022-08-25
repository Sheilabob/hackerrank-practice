#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    n=len(matrix)
    half = len(matrix)//2
    total = 0
    for i in range(half):
        for j in range(half):
            total += max((matrix[i][j]), (matrix[i][n-j-1]), (matrix[n-i-1][j]), (matrix[n-i-1][n-j-1]))
    return total

if __name__ == '__main__':