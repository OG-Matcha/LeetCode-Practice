# medium

'''
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.
'''

#　https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        data = set(i for i in range(n))

        for n in edges:
            if n[1] in data:
                data.remove(n[1]) 

        return list(data)

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        data = [True] * n

        for n in edges:
            data[n[1]] = False 

        return [i for i in range(len(data)) if data[i]]
    
# Time complexity = O(n) where n is the length of the edges
# Time complexity = O(n)
