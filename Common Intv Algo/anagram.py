from collections import Counter

def anagram(str1, str2):
    if sorted(str1) == sorted(str2):
    # if Counter(str1) == Counter(str2):
        return True
    else:
        return False






print(anagram('fried' , 'fired')) # true