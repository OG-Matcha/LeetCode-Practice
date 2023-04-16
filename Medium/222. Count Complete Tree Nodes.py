# medium

'''
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
'''

# https://leetcode.com/problems/count-complete-tree-nodes/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Dfs
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0

# Time complexity = O(n)
# Space complexity = O(n)

# Staightforward
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def counter(root, l = 1, r = 1):
            if not root:
                return 0

            left = right = root

            while left := left.left:
                l += 1
            while right := right.right:
                r += 1
            
            if l == r:
                return 2 ** l - 1 
            
            return 1 + counter(root.left) + counter(root.right)

        return counter(root)

# Time complexity = O(logn * logn)
# Space complexity = O(logn)