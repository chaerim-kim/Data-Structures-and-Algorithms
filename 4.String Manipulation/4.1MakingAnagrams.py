import math
import os
import random
import re
import sys
from collections import Counter

# find the number of deletions to be made in order for two strings to be anagrams
def makeAnagram(a, b):
    itsc = list((Counter(a) & Counter(b)).elements())
    # print(itsc)     #['r', 'x', 'w', 's', 'm', 'm', 'l', 'i', 'g', 'v']

    sum = (len(a) - len(itsc)) + (len(b) - len(itsc))
    # print(sum)
    return sum


########## Driver code ##########
makeAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke")
# Output: 30
#################################


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     a = input()
#     b = input()
#     res = makeAnagram(a, b)
#     fptr.write(str(res) + '\n')
#     fptr.close()
