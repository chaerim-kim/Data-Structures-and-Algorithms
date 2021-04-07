# iterative
# def canSum(targetSum, arr):
#     if targetSum == 0: return True
#     if targetSum < 0: return False
#
#     for i in arr:
#         remainder = targetSum-i
#
#         if canSum(remainder,arr) == True:
#             return True
#
#     return False

memo={}
def canSum(targetSum, arr):
    # print(memo)

    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False

    for i in arr:
        remainder = targetSum-i
        if canSum(remainder, arr) == True:
            # adding to memo
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


# canSum(7, [2,3,4,6])     # true

# print(canSum(7, [2,3,4,6]))     # true
print(canSum(8, [2,3,5]))         # true
# print(canSum(300, [7,14]))      # false
