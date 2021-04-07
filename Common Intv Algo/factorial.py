# def facto(n):
#     if n == 0: return 0
#     if n == 1: return 1
#
#     else:
#         return n*facto(n-1)

# recursive
memo={}
def facto(n):
    if n == 0: return 0
    if n == 1: return 1

    if n in memo.keys():
        return memo[n]

    else:
        memo[n] = n*facto(n-1)
    return memo[n]

print(facto(2))