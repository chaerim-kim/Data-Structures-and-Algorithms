import math
import os
import random
import re
import sys

# find maximum no of bribes such that it can move 2 forward to get to the final state
# form original ascending 1,2,3,4,5
def minimumBribes(q):
    count = 0

    # so if the difference is bigger than 2, it is too chaotic.
    for k,v in enumerate (q):
        if q[k] -(k+1) > 2:
            print("Too chaotic")
            return
        # Since no one can jump ahead of its original position by more than 2, so any value higher than q[i] can only be till index q[i] -2.

        # 그니까 이제 세개씩 잘라서 비교 - 그 어레이 숫자부터 -2 로 앞으로 해서
        # [1,2,5,3,4] 면 1,1 & 2,1 & 5,5, & 3,2/ 3,5 & 4,5/4,3
        for j in range (max(0,q[k]-2), k):
            print(q[k],q[j])
            if q[j] > q[k]:
                count+=1
    print (count)




########## Driver code ##########
minimumBribes([1,2,5,3,4])     # from 1,2,3,4,5
# Output: 2
#################################


# if __name__ == '__main__':
#     t = int(input())
#
#     for t_itr in range(t):
#         n = int(input())
#         q = list(map(int, input().rstrip().split()))
#         minimumBribes(q)
