#!/bin/python3

import math
import os
import random
import re
import sys


# check if all item in 'note' is in 'magazine'
def checkMagazine(magazine, note):
    flag = 0

    # sort the list for faster processing
    magazine.sort()
    note.sort()

    for item in note:
        if item not in magazine:
            flag = 1
            break
        else:
            magazine.remove(item)

    if flag == 1:
        print("No")
    else:
        print("Yes")

    return

    # if all item in note exists in magazine
    # elif (all(x in note for x in magazine)):
    #     print("Yes")

    # if note[i] in magazine:
    #     print (note[i])
    #     note.remove([note[i]])
    #     magazine.remove([note[i]])
    #
    #     if (len(note) == 0):
    #         print ("Yes")
    # return


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
