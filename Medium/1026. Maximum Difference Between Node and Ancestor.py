# medium

'''
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
'''

# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Dfs & Top down
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def dfs(root, maxi, mini):
            if not root:
                self.ans = max(self.ans, maxi - mini)
                return
            
            dfs(root.left, max(maxi, root.val), min(mini, root.val))
            dfs(root.right, max(maxi, root.val), min(mini, root.val))

        dfs(root, 0, 10000)

        return self.ans

# Time complexity = O(n)
# Space complexity = O(h)