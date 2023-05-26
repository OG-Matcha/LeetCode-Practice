# medium

'''
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
'''

# https://leetcode.com/problems/stone-game-ii/description/

# Logical Thinking
'''
dp[i, m] = maximum stones the current player can get from piles[i:] with M = m
A[i] = total stones of piles[i:]

when current player pick stones from i to i+x-1
-> the other player's stones: dp[i+x, max(m, x)]
-> total stones of current player: A[i] - dp[i+x, max(m, x)]

dp[i+x, max(m, x)] is the maximum stones the other player can get with the rest of the piles 
(for the other player the pile now starts from i+x and the value of M will be set to max(m,x) as per problem description). 

In order to figure out the best number of stones the current player can get, we take the total stones in all the piles there are currently and then subtract the best the other player can do on their turn (the next turn), given that we take the first x number of piles.

we want the current player gets maximum means the other player gets minimum
'''

# Dynamic Programming




from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]

        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= n:
                return piles[i]
            return piles[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))

        return dp(0, 1)

# Time comeplexity = O(n^3)
# Space comeplexity = O(n^2)
