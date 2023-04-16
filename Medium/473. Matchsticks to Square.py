# medium
# https://leetcode.com/problems/matchsticks-to-square/submissions/

'''
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. 
You want to use all the matchsticks to make one square. 
You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.
'''

# Dfs
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        if not matchsticks:
            return False
        
        if sum(matchsticks) % 4 != 0:
            return False
        
        side = sum(matchsticks) // 4
        
        matchsticks.sort(reverse=True)
        
        sums = [0 for _ in range(4)]
        
        def dfs(idx):
            
            if idx == len(matchsticks):
                return sums[0] == sums[1] == sums[2] == side
            
            for i in range(4):
                if sums[i] + matchsticks[idx] <= side:
                    sums[i] += matchsticks[idx]
                    
                    if dfs(idx + 1):
                        return True
                    sums[i] -= matchsticks[idx]
            
            return False
        
        return dfs(0)

# Time complexity = O(4 ^ n)
# Space complexity = O(n)

# Backtrack
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        if not matchsticks:
            return False
        
        length = sum(matchsticks) // 4
        
        if sum(matchsticks) / 4 != length:
            return False
        
        sums = [0] * 4
        matchsticks.sort(reverse=True)
        
        def backtrack(idx):
            
            if idx == len(matchsticks):
                return True
            
            for j in range(4):
                if sums[j] + matchsticks[idx] <= length:
                    sums[j] += matchsticks[idx]
                    
                    if backtrack(idx + 1):
                        return True
                    sums[j] -= matchsticks[idx]
            
            return False
        
        return backtrack(0)

# Time complexity = O(4 ^ n)
# Space complexity = O(n)

# Dyanmic programming
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        N = len(matchsticks)
        basket, rem = divmod(sum(matchsticks), 4)
        
        if rem or max(matchsticks) > basket: 
            return False
        
        @lru_cache(None)
        def dfs(mask):
            if mask == 0: return 0
            for j in range(N):
                if mask & 1 << j:
                    neib = dfs(mask ^ 1 << j)
                    if neib >= 0 and neib + matchsticks[j] <= basket:
                        return (neib + matchsticks[j]) % basket
            return -1
                    
        return dfs((1 << N) - 1) == 0

# Time complexity = O(2 ^ n * n)
# Space complexity = O(2 ^ n)