
import math
import os
import random
import re
import sys

# Split the array in d, and rotate to the left
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


########## Driver code ##########
rotLeft([1,2,3,4],2)
# Output: [3, 4, 1, 2]
#################################


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     nd = input().split()
#     n = int(nd[0])
#     d = int(nd[1])
#     a = list(map(int, input().rstrip().split()))
#     result = rotLeft(a, d)
#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')#
#     fptr.close()
