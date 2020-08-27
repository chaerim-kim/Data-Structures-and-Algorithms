
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    ans = 0
    level = 0
    lvlist = []
    hit_zero = False

    for i in range (0,n):
        if s[i] == 'U':
            level += 1
            lvlist.append(level)
        elif s[i] == 'D':
            level -= 1
            lvlist.append(level)
    print (lvlist)

    for i in range (1, n):
        if ((lvlist[i] == 0) and (lvlist[i-1] < 0)):
            ans += 1
        else:
            continue
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
