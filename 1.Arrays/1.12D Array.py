import math
import os
import random
import re
import sys

# print the
def hourglassSum(arr):
    val = 0
    val_list=[]

    # i = row, j = col
    for i in range (len(arr)-2):        # 4 reps
        for j in range (len(arr)-2):        # 4 reps
            # calculate the hourglass
            val = arr[i][j] + arr[i][j+1] + arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            # add all hourglass sum values to a list
            val_list.append(val)

    return max(val_list)


########## Driver code ##########
# hourglassSum()
# Output: 3
#################################


# if __name__ == "__main__":
#     arr = []
#
#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))
