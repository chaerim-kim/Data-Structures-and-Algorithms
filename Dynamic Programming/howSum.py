memo={}
def howSum(targetSum, arr):
    # if item in arr
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in arr:
        remainder = targetSum-num
        remainderresult = howSum(remainder, arr)

        if remainderresult is not None:
            return remainderresult.append(num)

    print(remainderresult)
    return None


print(howSum(7, [2,3,4,7]))     # true
print(howSum(8, [2,3,5]))         # true
# print(canSum(300, [7,14]))      # false
