# # legacy fibonacci
# def fibonacci(n):
# 	if n <= 2: return 1
# return fibonacci(n-1) +fib(n-2)

memo = {}       # so that all function access same memo
def fibonacci_memo(n):
    if n in memo: return memo[n]
    if n <= 2: return 1

    memo[n] = fibonacci_memo(n-1) +fibonacci_memo(n-2)
    return memo[n]

print(fibonacci_memo(8))
# print(fibonacci_memo(50))

# this takes way too long
# O(2^n), f(50) = 2^50 steps OMG