# medium

'''
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.
'''

# https://leetcode.com/problems/path-with-maximum-probability/description/


import collections


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        data = collections.defaultdict(list)
        q = collections.deque([start])

        for idx, (i, j) in enumerate(edges):
            data[i].append([j, idx])
            data[j].append([i, idx])

        res = [0] * n
        res[start] = 1

        while q:
            curr = q.popleft()

            for n, i in data.get(curr, []):
                if res[curr] * succProb[i] > res[n]:
                    res[n] = res[curr] * succProb[i]
                    q.append(n)

        return res[end]

# Time complexity = O(n * m) where n is the number of nodes and m is the length of edges
# Space complexity = O(n + m)
