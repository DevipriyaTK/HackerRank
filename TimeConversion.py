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
    temp=s[:-2]
    mins=s[2:8]
    if(s[len(s)-2:]=="PM"):
        hour=int(temp[:2])
        if(hour!=12):
            hour=hour+12
        str1=str(hour)
        ans=''.join((mins[:0],str1,mins[0:]))
        return ans
    else:
        hour=int(temp[:2])
        if(hour!=12):
            return temp
        else:
            hour="00"
            ans=''.join((mins[:0],hour,mins[0:]))
            return ans
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
