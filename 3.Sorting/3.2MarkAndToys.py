#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    bought = 0
    prices.sort()

    for i in range (len(prices)):
        if prices[i] < k:
            k = k-prices[i]
            bought+=1
    return bought



# Driver code
maximumToys([1,12,5,111,200,1000,10], 50)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     nk = input().split()
#
#     n = int(nk[0])
#
#     k = int(nk[1])
#
#     prices = list(map(int, input().rstrip().split()))
#
#     result = maximumToys(prices, k)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
