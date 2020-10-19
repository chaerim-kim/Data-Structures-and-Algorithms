#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    anagramList=[]
    # result = task in item in range
    substring = [s[i:j] for i in range(0,len(s)) for j in range(i+1,len(s)+1)]
    ssubstring = set(substring)
    print(ssubstring)

    for item in ssubstring:
        print(sorted(item))




    # print (ssubstring)
    # for i in range(len(substring)-1):
    #     for j in range(1,len(substring)):
    #         print(substring[i], substring[j])
    #         if sorted(substring[i]) == sorted(substring[j]):
    #             print("Anagram")
    #             anagramList.append(substring[i])
    #             anagramList.append(substring[j])
    #         else:
    #             print("nope")
    # print(set(anagramList))
    # print(len(set(anagramList)))
    # print(anagramList)



# driver code
sherlockAndAnagrams("abba")


# def is_anagram( string1, string2 ):
#     a = sorted(string1)
#     b = sorted(string2)
#     print(a,b)
#     if a == b:
#         print("Anagram")
#         return True
#     else:
#         print("Nope")
#         return False
#
#
# is_anagram("boo","aab")

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
