class Solution:
    def groupAnagrams(self, strs):
        result_obj = {}
        for i in range(len(strs)):
            potential_keys = self.sortString(strs[i])
            if potential_keys not in list(result_obj.keys()):
                result_obj[potential_keys] = [strs[i]]
            else:
                result_obj[potential_keys].append(strs[i])
        result = []
        for i in range(len(result_obj)):
            result.append(result_obj.get(list(result_obj.keys())[i]))
      
        print(result)




    def sortString(self, word):
        result = "".join(sorted(word))
        return result

test = Solution()
test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])