# https://www.hackerrank.com/challenges/counting-valleys/problem
"""
An avid hiker keeps meticulous records of their hikes. During the last hike
 that took exactly  steps, for every step it was noted if it was an uphill, 
 , or a downhill,  step. Hikes always start and end at sea level, and each step 
 up or down represents a  unit change in altitude. 
 
 We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with
 a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with
 a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, 
find and print the number of valleys walked through.

Example
Sample Input
Steps Count = 8
Path = UDDDUDUU
Sample Output = 1
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    m_v_flag = None
    m_v_count = [0,0]
    altitude = 0
    for step in path:
        altitude = (altitude+1) if step=='U' else (altitude-1)
        if m_v_flag is None:
            if altitude == -1:
                m_v_flag = 1
            elif altitude == 1:
                m_v_flag = 0
        if altitude == 0:
            m_v_count[m_v_flag]+=1
            m_v_flag = None
    print(m_v_count)
    return m_v_count[1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
