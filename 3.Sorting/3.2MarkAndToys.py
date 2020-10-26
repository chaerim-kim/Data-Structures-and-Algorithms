import math
import os
import random
import re
import sys

# max no of toys he could buy with money k
def maximumToys(prices, k):
    bought = 0
    prices.sort()

    for i in range (len(prices)):
        if prices[i] < k:
            k = k-prices[i]
            bought+=1
    return bought


########## Driver code ##########
maximumToys([1,12,5,111,200,1000,10], 50)
# Output: 4 ($ 1,5,10,12)
#################################

# if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # nk = input().split()
    # n = int(nk[0])
    # k = int(nk[1])
    # prices = list(map(int, input().rstrip().split()))
    # result = maximumToys(prices, k)
    # fptr.write(str(result) + '\n')
    # fptr.close()
