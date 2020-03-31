class Solution:
    # O(n^2)
    def maxArea(self, height):
        if len(height) == 0 or len(height) == 1:
            return 0
        max_num = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                if height[i] < height[j]:
                    area = height[i]*(j-i)
                    if area > max_num:
                        max_num = area
                else:
                    area = height[j]*(j-i)
                    if area > max_num:
                        max_num = area
        return max_num

    # O(n)
    def bettermaxArea(self, height):
        max_num = 0
        i = 0
        j = len(height) - 1
        while (i != j):
            if height[i] < height[j]:
                    area = height[i]*(j-i)
                    if area > max_num:
                        max_num = area
                    i += 1
            else:
                    area = height[j]*(j-i)
                    if area > max_num:
                        max_num = area
                    j -= 1
                
        return max_num


test = Solution()
print(test.maxArea([1,8,6,2,5,4,8,3,7]))
        