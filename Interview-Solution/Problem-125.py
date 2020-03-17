class Solution:
    def isPalindrome(self, s):
        if s == "":
            return True
        if s == " ":
            return True

        i = 0
        j = -1
        helper = True
        while (i+(0-j) != len(s) and (i+(-j) != len(s)+1)):
            if not(s[j].islower() or s[j].isupper() or s[j].isdigit()):
                j -= 1
            elif not(s[i].islower() or s[i].isupper() or s[i].isdigit()):
                i += 1
            else:
                if (s[i].lower() == s[j].lower()):
                    i += 1
                    j -= 1
                else:
                    helper = False
                    return helper
        return helper


test = Solution()
print(test.isPalindrome(":0b::::"))
