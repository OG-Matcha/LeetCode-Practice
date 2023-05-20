# medium

'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
'''

# https://leetcode.com/problems/evaluate-division/description/

import collections

# Bfs
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        data = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            data[x][y] = v
            data[y][x] = 1 / v

        def bfs(src, dst):
            if src not in data and dst not in data:
                return -1.0

            q = [(src, 1.0)]
            seen = set()

            for x, v in q:
                if x == dst:
                    return v

                seen.add(x)

                for y in data[x]:
                    if y not in seen:
                        q.append((y, v * data[x][y]))

            return -1.0

        return [bfs(s, d) for s, d in queries]

# Time comeplixity = O(n + n * q) where n is the number of equations and q is the number of queries.
# Space comeplixity = O(n + q)


import itertools

# Floyd–Warshall (https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        data = collections.defaultdict(dict)

        for (x, y), v in zip(equations, values):
            data[x][x] = data[y][y] = 1.0
            data[x][y] = v
            data[y][x] = 1 / v

        for k, i, j in itertools.permutations(data, 3):
            if k in data[i] and j in data[k]:
                data[i][j] = data[i][k] * data[k][j]
                
        return [data[num].get(den, -1.0) for num, den in queries]

# Time comeplixity = O(n ^ 3) where n is the number of equations and q is the number of queries.
# Space comeplixity = O(n + q)