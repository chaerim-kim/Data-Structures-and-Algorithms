import math
import os
import random
import re
import sys

# Greedy so first round = original price. second round = (round+1)*price
# k = number of peepes
def getMinimumCost(k, arr):
    n = len(arr)
    cost = 0

    # if there are more flowers than peeps they can buy all with original price
    if k >= n:
        cost = sum(arr)
        return cost

    # sort the array to give the most exp to people first
    arr.sort(reverse=True)

    for i in range (n):
        cost += (int (i/k)+1) * arr[i]
        print (cost)


########## Driver code ##########
getMinimumCost(3, [1,3,5,7,9])
# Output: 21 + 6 + 2 = 29
#################################


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     nk = input().split()
#     n = int(nk[0])
#     k = int(nk[1])
#     c = list(map(int, input().rstrip().split()))
#     minimumCost = getMinimumCost(k, c)
#     fptr.write(str(minimumCost) + '\n')
#     fptr.close()
