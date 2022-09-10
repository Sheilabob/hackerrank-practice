#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks.sort()
    i = len(sticks) - 3
    while 1 >= 0 and sticks[i] + sticks[i+1] <= sticks[i+2]:
        i -= 1
    if i >= 0:
        return [sticks[i], sticks[i+1], sticks[i+2]]
    else:
        return [-1]
    # triangle_lists = []
    # if n==3:
    #     if sticks[0]+sticks[1] > sticks[2]:
    #         return sticks
    #     else:
    #         return [-1]
    # for i in range(n-2):
    #     for j in range(i+1,n-1):
    #         for k in range(j+1,n):
    #             if sticks[i] + sticks[j] > sticks[k]:
    #                 x=[sticks[i],sticks[j],sticks[k]]
    #                 if x not in triangle_lists:
    #                     triangle_lists.append(x)
    # if len(triangle_lists) == 0:
    #     return [-1]
    # o = len(triangle_lists)
    # longest_sides=[]
    # shortest_sides=[]
    # for i in range(o):
    #     longest_sides.append(triangle_lists[i][2])
    # longest_longest_side = max(longest_sides)
    # p=len(longest_sides)
    # index_longest=[]
    # for i in range(p):
    #     if longest_sides[i] == longest_longest_side:
    #         index_longest.append(i)
    # q=len(index_longest)
    # if len(index_longest) > 1:
    #     for i in range(q):
    #         shortest_sides.append(triangle_lists[index_longest[i]][0])
    #     shortest_side_max = max(shortest_sides)
    #     return index_longest.index(shortest_side_max)
    # else:
    #     return triangle_lists[index_longest[0]]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
