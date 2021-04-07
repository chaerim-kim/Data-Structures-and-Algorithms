# 10번 동안 1~10까지 랜덤한 숫자를 출력하여 중복된 숫자가 있을 경우 true, false를 리턴하라
import random

def print_random():
    lis=[]

    for i in range(10):
        lis.append(random.randint(1,10))
    print(lis)

    if len(set(lis)) != 10:
        return True
    return False

print(print_random())