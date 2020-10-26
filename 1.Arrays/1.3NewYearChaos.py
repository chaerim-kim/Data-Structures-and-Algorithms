import math
import os
import random
import re
import sys

# find maximum no of bribes such that it can move 2 forward to get to the final state
# form original ascending 1,2,3,4,5
def minimumBribes(q):
    bribe = 0

    # q = [2,1,5,3,4]
    # i+1 = 1,2,3,4,5
    # so if the difference is bigger than 2, it is too chaotic.
    for i, element in enumerate (q):
        if  q[i] - (i+1) > 2:
            print ('Too chaotic')
            return

        # This works, but it causes timeout - hence we need a smarter way to execute the loop comparison.
        # for j in range(i+1, len(q)):
        #     if q[j] < q[i]:
        #         bribe+=1

        # Since no one can jump ahead of its original position by more than 2, so any value higher than q[i] can only be till index q[i] -2.
        # we only compare values that are two ahead.
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribe+=1
    print(bribe)


########## Driver code ##########
minimumBribes([2,1,5,3,4])     # from 1,2,3,4,5
# Output: 3
#################################


# if __name__ == '__main__':
#     t = int(input())
#
#     for t_itr in range(t):
#         n = int(input())
#         q = list(map(int, input().rstrip().split()))
#         minimumBribes(q)
