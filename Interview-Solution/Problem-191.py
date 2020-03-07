class Solution:
    def hammingWeight(self, n):
        result = 0
        string_n = bin(n)[2:]
        for x in string_n:
            if x == '1':
                result += 1
        return result

test = Solution()
print(test.hammingWeight(11))