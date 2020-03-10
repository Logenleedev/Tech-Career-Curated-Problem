class Solution:
    def isValid(self, s):
        if len(s) == 0:
            return True
        key_dict = {")":"(", "]":"[", "}":"{"}
        Left_part = ["(", "{", "["]
        stack = []
        for i in range(len(s)):
            if s[i] in Left_part:
                stack.append(s[i])
            else:
                if len(stack) != 0:
                    if stack[-1] == key_dict[s[i]]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
test = Solution()
print(test.isValid("]"))
