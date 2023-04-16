# medium

'''
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 10^9 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.
'''

# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Dfs
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        self.res = self.total = 0

        def dfs(root):
            if not root: 
                return 0
            curr = dfs(root.left) + dfs(root.right) + root.val
            self.res = max(self.res, curr * (self.total - curr))
            return curr

        self.total = dfs(root)
        dfs(root)
        return self.res % 1000000007

# Time complexity = O(n)
# Space complexity = O(h)