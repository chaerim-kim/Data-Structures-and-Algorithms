import math
import os
import random
import re
import sys
from collections import Counter

# Complete the whatFlavors function below.
def whatFlavors(cost, money):

    dic = dict()
    for pos,v in enumerate(cost):
        if v not in dic:
            dic[money-v] = pos+1
        else:
            print(dic[v], pos+1)

        # print(dic)
        # if money > v:
        #     rm = money-v
        #
        #     if rm in cost and v+rm ==money :
        #         if rm == v:
        #             # print(cost[i:])
        #             print("boop")
        #             print(i, cost[i:].index(rm)+i+1)
        #             break
        #         else:
        #             print (v,rm)
        #             print(i,cost.index(rm)+1)
        #             break



whatFlavors([2,2,4,3],4)

# if __name__ == '__main__':
#     t = int(input())
#     for t_itr in range(t):
#         money = int(input())
#         n = int(input())
#         cost = list(map(int, input().rstrip().split()))
#         whatFlavors(cost, money)
