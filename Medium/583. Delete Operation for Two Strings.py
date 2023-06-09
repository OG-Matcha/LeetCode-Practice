# medium

'''
Given two strings word1 and word2, 
return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.
'''

# Solution I - Memoization - Top Down
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        @cache
        def lcs(i, j): # find longest common subsequence
            if i == m or j == n:
                return 0            
            return 1 + lcs(i + 1, j + 1) if word1[i] == word2[j] else max(lcs(i + 1, j), lcs(i, j + 1))                               
        # subtract the lcs length from both the strings 
        # the difference is the number of characters that has to deleted
        return m + n - 2 * lcs(0, 0)

# Time - O(m * n) - to explore all paths
# Space - O(m * n) - for cache and recursive call stack

# Solution II - Tabulation - Bottom Up
class Solution:       
    def minDistance(self, word1: str, word2: str) -> int:
        
        if len(word1) > len(word2):
            word2, word1 = word1, word2        
        
        m, n = len(word1), len(word2)
        prev = [0] * (m + 1)
        
        for i in range(n - 1, -1, -1):
            curr = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                if word1[j] == word2[i]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(curr[j + 1], prev[j])
            prev = curr
            
        return m + n - 2 * prev[0]

# Time - O(m * n)
# Space - O(min(m,n)) - for the dp array