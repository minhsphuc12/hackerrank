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
    su = sum(arr)
    print(str(su-max(arr)), str(su-min(arr)))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    arr = [1,2,4,6,8]
    miniMaxSum(arr)
