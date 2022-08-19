#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    letter_array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    lowercase_s = s.lower()
    for letter in lowercase_s:
        if letter in letter_array:
            letter_array.remove(letter)
    if len(letter_array) == 0:
        return 'pangram'
    else:
        return 'not pangram'
            
    # turn everything lowercase
    # pop each letter in the array as it turns up
    #if array is empty, return true

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()