#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min,max=0,0
    arr.sort()
    for i in range(0,len(arr)-1):
        min=min+arr[i]
    for j in range(1,len(arr)):
        max=max+arr[j]
    print(min,max)
    


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
