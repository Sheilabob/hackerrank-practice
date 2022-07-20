#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    #maybe convert whole thing into an array?
    listTime=[]
    listTime[:0]=s
    if s[-2]=='A' and s[0]=='1' and s[1]=='2':
        listTime[0]='0'
        listTime[1]='0'
        listTime.pop(-1)
        listTime.pop(-1)
        return ("".join(listTime))
    elif s[-2]=='A':
        listTime.pop(-1)
        listTime.pop(-1)
        return ("".join(listTime))
    elif s[0]=='1' and s[1]=='2' and s[-2]=='P':
        listTime.pop(-1)
        listTime.pop(-1)
        return ("".join(listTime))
    else:
        listTime.pop(-1)
        listTime.pop(-1)
        convert = listTime[slice(2)]
        num1 = int("".join(convert))
        num2 = num1 + 12
        num2 = str(num2)
        num2List=[]
        num2List[:0]=num2
        listTime[0]=num2List[0]
        listTime[1]=num2List[1]
        return ("".join(listTime))
    # if starts with 12 and ends with AM, change start to 00, if arr[0]=1 and arr[1] = 2 and arr[8]=A, arr[0]=0, arr[1]=0, slice off arr[8] and arr[9]
    # if ends with AM, return same
    #if ends with PM, add 12 to beginning and return

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()