class Solution:
    def bruteforcemaxSubArray(self, nums):
        # O(n^3)
        if len(nums) != 0:
            result = []
            for i in range(len(nums)):
                for j in range(i+1, len(nums)+1):
                    part_sum = 0
                    for z in range(i, j):
                        part_sum += nums[z]
                        result.append(part_sum)
            return max(result)
        else:
            return 0
    
    def improvedmaxSubArray(self, nums):
        # O(n^2)
        if len(nums) != 0:
            result = []
            for i in range(len(nums)):
                result.append(nums[i])
                for j in range(i+1, len(nums)):
                    result.append(result[-1]+nums[j])

            return max(result)
        else:
            return 0
        
    def bestmaxSubarray(self, nums):
        # O(n)
        if len(nums)!= 0:
            result = [nums[0]]
            for i in range(1, len(nums)):
                best_max = max(result[-1]+nums[i], nums[i])
                result.append(best_max)

            biggest_sum = result[0]
            for i in range(len(result)):
                if biggest_sum <= result[i]:
                    biggest_sum = result[i]
            return biggest_sum
        else:
            return 0
            

        

test = Solution()
print(test.bestmaxSubarray([-2,1,-3,4,-1,2,1,-5,4]))
