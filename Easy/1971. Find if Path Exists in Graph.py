# easy

'''
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise. 
'''

# https://leetcode.com/problems/find-if-path-exists-in-graph/solutions/2814240/python-union-find-using-rank/

# Dfs & Defaultdict
import collections
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        data = collections.defaultdict(list)

        for node1, node2 in edges:
            data[node1].append(node2)
            data[node2].append(node1)
        
        def dfs(source, destination, seen):
            if source == destination:
                return True
            if source in seen:
                return False
            
            seen.add(source)

            for i in data[source]:
                if dfs(i, destination, seen):
                    return True
            
            return False
        
        seen = set()

        return dfs(source, destination, seen)
