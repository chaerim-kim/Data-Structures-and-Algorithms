import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    check_list=[]
    count = 0
    for i in range(n):
        if ar[i] not in check_list:
            check_list.append(ar[i])
        else:
            check_list.remove(ar[i])
            count+=1
            print(count)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
