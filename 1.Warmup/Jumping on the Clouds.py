
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    ans = 0
    current_index = 0
    goal = len(c)-1

    while (current_index < goal):
        if ((current_index + 2 <= goal) and (c[current_index+2] == 0)):
            current_index += 2
            ans += 1

        elif (c[current_index+1] == 0 ):
            current_index += 1
            ans += 1

    return ans



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
