#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    n = len(grades)
    rounded_grades = []
    for i in range(n):
        if grades[i] < 38:
            rounded_grades.append(grades[i])
        elif grades[i]%5 > 2:
            new_grade = grades[i] - grades[i]%5 + 5
            rounded_grades.append(new_grade)
        else:
            rounded_grades.append(grades[i])
    return rounded_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
