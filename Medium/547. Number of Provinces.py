# medium

'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
'''

# https://leetcode.com/problems/number-of-provinces/description/

# Dfs


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(city):
            for i, v in enumerate(isConnected[city]):
                if v and i not in seen:
                    seen.add(i)
                    dfs(i)

        seen = set()
        count = 0

        for i in range(len(isConnected)):
            if i not in seen:
                dfs(i)
                count += 1

        return count

# Time comeplxity = O(n^2) where n is the number of cities
# Space comeplxity = O(n)
