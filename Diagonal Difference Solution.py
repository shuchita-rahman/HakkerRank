#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr, n):
    sum1 = 0
    sum2 = 0;

    for i in range(0,n):
          for j in range(0, n):
             if i == j:
                 sum1 = sum1 + arr[i][j]
             if i+ j == n - 1:
                 sum2 = sum2 + arr[i][j]
    return abs(sum1 - sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
