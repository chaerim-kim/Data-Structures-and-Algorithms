import math
import os
import random
import re
import sys
from collections import Counter

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    dict = {}

    for i,v in enumerate(cost,start=1):
        if v not in dict and v < money:
            dict[money-v] = [i,v]
        else:
            print((dict[v])[0],i)
            break
    # print (dict)

    # c1 = Counter(money)


whatFlavors([2,2,4,3],4)

# if __name__ == '__main__':
#     t = int(input())
#     for t_itr in range(t):
#         money = int(input())
#         n = int(input())
#         cost = list(map(int, input().rstrip().split()))
#         whatFlavors(cost, money)
