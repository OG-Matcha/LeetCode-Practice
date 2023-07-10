# easy

'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
'''

# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return 0

            if not root.left or not root.right:
                return dfs(root.left) + dfs(root.right) + 1

            return min(dfs(root.left), dfs(root.right)) + 1

        return dfs(root)

# Time complexity = O(n) where n is the number of nodes in the binary tree
# Space complexity = O(n)
