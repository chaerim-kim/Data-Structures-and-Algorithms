import math
import os
import random
import re
import sys
from collections import Counter

# PRint 'Yes' if the characters occur the same amount of time with one deletion
# so abcc : Yes bc can remove one 'c'
def isValid(s):
    c1 = Counter(s)
    freq = Counter(c1.values())     # Counter({2: 2, 1: 1})
    print(c1)
    # if there is only one type
    # s = a or s = aabbccddeeff --> all has 2
    if len(freq) == 1:
        return "YES"

    mostcommon = max(freq.keys())
    leastcommon = min(freq.keys())

    if mostcommon - leastcommon == 1 and (freq[leastcommon] == 1 or freq[mostcommon]==1):
        return "YES"

    if mostcommon - leastcommon != 1:
        # for cases [3,2,2,1]
        if len(freq.keys())> 2:
            return "NO"

        if leastcommon == 1 and freq[leastcommon] ==1:
            return "YES"
    return "NO"


########## Driver code ##########
isValid("aabbccddeefghi")
# Counter({2: 5, 1: 4})
# Output: NO bc occurencies are to high - 5,4 should be 5,1
#################################


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     s = input()
#     result = isValid(s)
#     fptr.write(result + '\n')
#     fptr.close()
