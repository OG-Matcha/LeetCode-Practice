# medium

'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        length = len(s)
        self.count = 0
        
        def dfs(l, r):
            if l >= 0 and r < length and s[l] == s[r]:
                self.count += 1
                dfs(l-1, r+1)
                
        for i in range(length):
            dfs(i, i)
            dfs(i, i+1)
            
        return self.count

