# easy

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        res = ""
        strs.sort()
        for i in strs[0]:
            if strs[-1].startswith(res + i):
                res += i
            else:
                break
        return res

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        result = ""
        maxi, mini = max(strs), min(strs)
        
        for i in mini:
            if maxi.startswith(result + i):
                result += i
            else:
                break
        return result