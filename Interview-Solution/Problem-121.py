class Solution:
    def maxProfit(self, nums):
        if len(nums)==0:
            return 0
        else:
            profit = 0
            for i in range(len(nums)-1):
                for j in range(i+1, len(nums)):
                    earning = nums[j] - nums[i]
                    if earning > profit:
                        profit = earning
            return profit

test = Solution()
print(test.maxProfit([]))
print(test.maxProfit([7,6,4,3,1]))
