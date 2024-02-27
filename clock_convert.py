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
    # s = '07:05:45PM'
    am_pm = s[-2:]
    mid = s[2:-2]
    h = int(s[:2])
    if am_pm == 'AM':
        hn = 0 if h == 12 else h
    if am_pm == 'PM':
        hn = 12 if h == 12 else h + 12
    hn
    hn_text = '{:02}'.format(hn)
    return f'{hn_text}{mid}'
    

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
