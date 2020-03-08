class Solution:
    def productExceptSelf(self, nums):
        Left_list = []
        Right_list = []

        Left_list.append(1)
        Right_list.append(1)
        
        Left_product = 1
        for i in range(1, len(nums)):
            Left_product = nums[i-1]*Left_product
            Left_list.append(Left_product)
        
        Right_product = 1
        for i in range(-2, -(len(nums)+1), -1):
            Right_product = nums[i+1]*Right_product
            Right_list.insert(0, Right_product)
        
        result = []
        for i in range(len(nums)):
            result.append(Left_list[i]*Right_list[i])
        return result
test = Solution()
print(test.productExceptSelf([1,2,3,4]))