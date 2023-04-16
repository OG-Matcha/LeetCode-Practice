# easy

'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Dfs


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root):

            if not root:
                return 0

            return 1 + max(dfs(root.left), dfs(root.right))

        return dfs(root)

# Time complexity = O(n) where n is the number of nodes in the tree
# Space complexity = O(h) where h is the high of the tree for recursive stack
