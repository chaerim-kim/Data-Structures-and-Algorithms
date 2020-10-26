import math
import os
import random
import re
import sys
import time

# find the min no. of swaps to get sorted array
def minimumSwaps(arr):
    corr_idx = 0
    count = 0

    for idx in range(len(arr)):
        correct_val = idx + 1

        while (arr[idx] != correct_val):
            # search for the index of correct value !!!-> this causes timeout for large arr
            # corr_idx = arr.index(correct_val)

            # We send the value to its literal position in the array. but -1 bc of zero-indexing.
            # e.g. In [4,3,1,2], we send 4 to 4th position, but -1: hence arr[3]
            corr_idx = arr[idx]-1

            # swap two values
            arr[idx], arr[corr_idx] = arr[corr_idx], arr[idx]
            # print(index_dict)

            # increment
            count += 1

    return count


########## Driver code ##########
print(minimumSwaps([4,3,1,2]))
# Output: 3
#################################


# # if __name__ == '__main__':
#     t0 = time.time()
#     print(minimumSwaps([4,3,1,2]))
#     t1 = time.time()
#     print(t1-t0)
#     range slicing
