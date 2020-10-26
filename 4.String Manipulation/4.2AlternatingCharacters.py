import math
import os
import random
import re
import sys

# Delete the string so that there are no repeated strings nect to each other - make the stirngs alternate
def alternatingCharacters(s):
    count = 0
    s = list(s) # split the string into characters

    for i in range(0,len(s)-1):
        if s[i] == s[i+1]:
            count +=1
    return count


########## Driver code ##########
alternatingCharacters("AAABBB")
# Output: 4
#################################

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     q = int(input())
#     for q_itr in range(q):
#         s = input()
#         result = alternatingCharacters(s)
#         fptr.write(str(result) + '\n')
#     fptr.close()
