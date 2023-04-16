# easy

'''
Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], 
which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. 
If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. 
Your goal is to maximize the number of your content children and output the maximum number.
'''

# Brute-force
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        ans = 0
        
        for i in range(len(s)):
            if g and s[i] >= g[0]:
                ans += 1
                g.pop(0)
            
        return ans

# Two-pointer
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = 0
        j = 0
        
        sum = 0
        g.sort()
        s.sort()
        
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:                
                sum += 1
                i += 1
                j += 1
            else:
                j += 1
                
        return sum