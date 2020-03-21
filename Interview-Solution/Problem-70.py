class Solution:
    def climbStairs(self, n):
        dp = []
        dp.append(1)
        dp.append(1)
        for i in range(2, n+1):
            result = dp[i-1] + dp[i-2]
            dp.append(result)
        return dp[-1]

test = Solution()
print(test.climbStairs(3))
