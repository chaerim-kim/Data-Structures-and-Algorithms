# # Brute forcing
# memo = {}
# def maxSubArray(self, nums: List[int]) -> int:
#     boop=[]
#     if len(nums) == 1: return nums[0]
#
#     # first brute force and add all possibilities
#     for i in range (len(nums)):
#         for j in range (i+1, len(nums)+1):
#             boop.append(sum(nums[i:j]))
#     return max(boop)



def maxSubArray(self, A):

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
            print(num, curSum, maxSum)


        return maxSum

print(maxSubArray(self, [5,4,-1,7,8]))
