memo = {}
def gridTraveler(n, m):
    # as we are moving, we are shrinking the size of the problem scope
    keyy = str(n)+','+str(m)

    if keyy in memo: return memo[keyy]
    if n == 0 or m == 0: return 0
    if n == 1 and m == 1: return 1

    # get the sum of me going downward and rightward
    memo[keyy]= gridTraveler(n-1,m) + gridTraveler(n,m-1)
    return memo[keyy]


print(gridTraveler(1,1))    #1
print(gridTraveler(2,3))    #3
print(gridTraveler(3,2))    #3
print(gridTraveler(3,3))    # 6
print(gridTraveler(12,12))