#!/bin/python3

import math
import os
import random
import re
import sys

def sherlockAndAnagrams(s):
    dict ={}
    ans=0

    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            # get all the substrings
            sliced = s[i:j]
            # sort the substirngs, and then join them again
            joined = ''.join(sorted(sliced))

            if joined not in dict:
                dict[joined] = 1
            # if the substring already exists in dict, count up ans and dict value
            else:
                ans += dict[joined]
                dict[joined] += 1
    print(ans)
    return ans

    # # list comprehension version
    # # get all substrings of a string & sort the substring, then rejoin them
    # substring = [''.join(sorted(s[i:j])) for i in range(0,len(s)) for j in range(i+1,len(s)+1)]
    # print(substring)        #['a', 'ab', 'abb', 'abba', 'b', 'bb', 'bba', 'b', 'ba', 'a']
    #
    # # for each substring, get the character frequency key
    # for item in substring:
    #     if item not in dict:
    #         dict[item] = 1
    #
    #     # if the substring already exists in dict, count up ans and dict value
    #     else:
    #         ans += dict[item]
    #         dict[item] +=1
    # print(ans)




# driver code
sherlockAndAnagrams("cdcd")

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     q = int(input())
#
#     for q_itr in range(q):
#         s = input()
#
#         result = sherlockAndAnagrams(s)
#
#         fptr.write(str(result) + '\n')
#
#     fptr.close()
