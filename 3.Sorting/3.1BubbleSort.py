import math
import os
import random
import re
import sys

# Number of swaps to sort the array using buuble sort
def countSwaps(a):
    count = 0
    n = len(a)
    # edge case where array is sorted - O(nlogn)
    if(a == sorted(a)):
        print ("Array is sorted in 0 swaps.")

    # bubble sort
    for i in range(0,n):
        for j in range (0,n-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                count +=1

    if count > 0:
        print ("Array is sorted in " + str(count)+ " swaps.")
    print ("First Element: " + str(a[0]))
    print ("Last Element: " + str(a[n-1]))

    return


########## Driver code ##########
countSwaps([5,4,3,2,1])
# Output: 10 (4,3,2,1 times each)
#################################


# if __name__ == '__main__':
#     n = int(input())
#     a = list(map(int, input().rstrip().split()))
#     countSwaps(a)
