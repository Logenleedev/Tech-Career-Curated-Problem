class Solution:
    def containsDuplicate(self, nums):
        array = sorted(nums)
        for i in range(len(array)-1):
            if array[i] == array[i+1]:
                return True
        return False
    
test = Solution()
print(test.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(test.containsDuplicate([1,2,3]))
