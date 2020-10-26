import math
import os
import random
import re
import sys

# Find the min abs diff in the given array
def minimumAbsoluteDifference(arr):
    arr.sort()
    # consider first pair of diff as min
    minn = abs(arr[0]-arr[1])
    for i in range (len(arr)-1):
            if abs(arr[i]-arr[i+1]) < minn:
                minn = abs(arr[i]-arr[i+1])
    print(abs(minn))
    return


########## Driver code ##########
minimumAbsoluteDifference([3,-7,0])
# Output: 3         |3-0|
#################################



# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     n = int(input())
#     arr = list(map(int, input().rstrip().split()))
#     result = minimumAbsoluteDifference(arr)
#     fptr.write(str(result) + '\n')
#     fptr.close()
