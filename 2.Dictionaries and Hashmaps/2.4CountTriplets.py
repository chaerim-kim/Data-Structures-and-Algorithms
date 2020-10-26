import math
import os
import random
import re
import sys
from collections import Counter

# From array, find the number of ascending triplets that can be found
def countTriplets(arr, r):
    count = 0
    # elements are stored as dictionary keys and their counts are stored as dictionary values.
    r2 = Counter()
    r3 = Counter()

    for i in arr:
        if i in r3:
            count = count + r3[i]
        if i in r2:
            r3[i*r] = r3[i*r] + r2[i]
        r2[i*r] +=1
    print (count)

    # geom_list=[]
    # ans=0
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
    #
    # for item in sliced:
    #     if len( list((Counter(item) & Counter(arr)).elements())) != 0:
    #         ans += 1
    # print(ans)

########## Driver code ##########
countTriplets([1,4,16,64], 4)
# (1,4,16) (4,16,64)
# Output: 2
#################################


# # if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     nr = input().rstrip().split()
#     n = int(nr[0])
#     r = int(nr[1])
#     arr = list(map(int, input().rstrip().split()))
#     ans = countTriplets(arr, r)
#     fptr.write(str(ans) + '\n')
#     fptr.close()
