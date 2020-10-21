#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the countTriplets function below.
def countTriplets(arr, r):
    geom_list=[]
    ans=0
    dict = {}
    newdict={}
    count = 0

    # for i in range (min(arr), len(arr)):
    #     # add first element
    #     if len(geom_list) == 0:
    #         geom_list.append(min(arr))
    #     if geom_list[i-1] * r <= max(arr):
    #         geom_list.append( geom_list[i-1] * r)
    #
    # # sliced into every 3 triplets
    # sliced = [geom_list[i:i+3] for i in range (len(geom_list)-2)]
    # print (sliced)      # [[1, 5, 25], [5, 25, 125]
    #
    # # arr = [1,5,5,25,125]
    # # b = item
    # # a = arr
    # s2=" ".join(str(i) for i in arr)
    # print(s2)
    #
    # for item in sliced:
    #     s1 = " ".join(str(i) for i in item)
    #     print (s1)
    #
    # for i in range (len(arr)-1):
    #     if s1 in s2:
    #         count +=1
    # print (count)

    r2 = Counter()
    r3 = Counter()

    for i in arr:
        if i in r3:
            count = count + r3[i]
        if i in r2:
            r3[i*r] = r3[i*r] + r2[i]
        r2[i*r] +=1
    print( count)


# Driver code
countTriplets([1,4,16,64], 4)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     nr = input().rstrip().split()
#
#     n = int(nr[0])
#
#     r = int(nr[1])
#
#     arr = list(map(int, input().rstrip().split()))
#
#     ans = countTriplets(arr, r)
#
#     fptr.write(str(ans) + '\n')
#
#     fptr.close()
