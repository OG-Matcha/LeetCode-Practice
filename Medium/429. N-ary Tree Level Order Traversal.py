# medium

'''
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
'''

# https://leetcode.com/problems/n-ary-tree-level-order-traversal/


# Bfs & Deque
from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        
        q = deque([root])
        ans = []
        
        while q:
            level = []
            
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)
                
                for val in curr.children:
                    q.append(val)
            
            ans.append(level)
        
        return ans

# Time complexity = O(n)
# Space complexity = O(n)

# Dfs
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        def dfs(root, level):
            if not root:
                return []
            if level == len(ans):
                ans.append([])
            ans[level].append(root.val)
            for val in root.children:
                dfs(val, level + 1)
        
        ans = []
        dfs(root, 0)
        return ans

# Time complexity = O(n)
# Space complexity = O(h)