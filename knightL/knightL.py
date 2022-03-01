#!/bin/python3
"""
https://www.hackerrank.com/challenges/knightl-on-chessboard/problem?isFullScreen=true
"""


import math
import os
import random
import re
import sys

#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def knightlOnAChessboard(n):
    # Write your code here
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
