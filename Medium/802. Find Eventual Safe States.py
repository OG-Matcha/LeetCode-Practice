# medium

'''
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
'''

# https://leetcode.com/problems/find-eventual-safe-states/description/

import collections


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        need = [0] * len(graph)
        status = [[] for _ in range(len(graph))]

        for i in range(len(graph)):
            for node in graph[i]:
                status[node].append(i)
                need[i] += 1

        q = collections.deque()

        for i in range(len(graph)):
            if not need[i]:
                q.append(i)

        safe = [False] * len(graph)

        while q:
            curr = q.popleft()
            safe[curr] = True

            for node in status[curr]:
                need[node] -= 1

                if not need[node]:
                    q.append(node)

        return [i for i, v in enumerate(safe) if v]

# Time complexity = O(m + n) # where n is the number of nodes and m is number of edges in the graph
# Space complexity = O(m + n)
