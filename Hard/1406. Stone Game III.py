# hard

'''
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 stones from the first remaining stones in the row.

The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.
'''

# https://leetcode.com/problems/stone-game-iii/description/

# Dynamic Programming


import collections


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = stoneValue[i] - dp[i + 1]
            if i + 2 <= n:
                dp[i] = max(dp[i], stoneValue[i] +
                            stoneValue[i + 1] - dp[i + 2])
            if i + 3 <= n:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1]
                            + stoneValue[i + 2] - dp[i + 3])
        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"

# Time complexity = O(n)
# Space complexity = O(n)


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = collections.deque([0] * 3)
        postSum = 0

        for i in range(n - 1, -1, -1):
            postSum += stoneValue[i]
            newValue = postSum - min(dp)
            dp.pop()
            dp.appendleft(newValue)

        pointsAlice = dp[0]
        if pointsAlice * 2 > postSum:
            return 'Alice'
        elif pointsAlice * 2 < postSum:
            return 'Bob'
        else:
            return 'Tie'

# Time complexity = O(n)
# Space complexity = O(1)
