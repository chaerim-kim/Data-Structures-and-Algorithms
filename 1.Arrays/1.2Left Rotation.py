
import math
import os
import random
import re
import sys

# Complete the rote rotLeft function below.
def rotLeft(a, d):
    # split the array into two, then append the two in reversed order
    return a[d:] + a[:d]



#     for i in range(d):
#         output = leftRotatebyOne(a, n)
#     return output
#
# def leftRotatebyOne(a, n):
#     temp = a[0]
#
#     for i in range (n-1):
#         a[i] = a[i+1]
#     a[n-1] = temp
#     return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
