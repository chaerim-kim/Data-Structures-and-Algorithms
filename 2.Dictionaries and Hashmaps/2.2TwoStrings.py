#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    ans="YES"

    # split the word into a single character and aggregate it into a set to remove duplicates
    splitted_s1 =set(list(s1))
    splitted_s2 =set(list(s2))

    # if there exists no intersection, return no
    if splitted_s1.isdisjoint(splitted_s2):
        ans="NO"

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
