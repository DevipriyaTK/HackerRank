#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    arr.sort()
    positive,zero,negative=0,0,0
    result=[]
    i,j,k,l=0,0,0,0
    while i < len(arr):
        if(arr[i]<0):
            j=j+1
            negative=j/len(arr)
        elif(arr[i]==0):
            k=k+1
            zero=k/len(arr)
        elif(arr[i]>0):
            l=l+1
            positive=l/len(arr)  
        i=i+1
    result.append(positive)
    result.append(negative)
    result.append(zero)
    return result

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    results=plusMinus(arr)
    for a in results:
        print('%.6f' % a)
