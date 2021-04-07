# # iterative
# def fib(n):
#     if n == 0: return 0
#     if n == 1: return 1
#
#     return fib(n-1) +fib(n-2)

# recursive
memo = {}
def fib(n):
    if n in memo.keys():
        return memo[n]
    if n == 0: return 0
    if n == 1: return 1

    else:
        memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


print(fib(10))      # 55