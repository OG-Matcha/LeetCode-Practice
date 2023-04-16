# easy

'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def helper(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            else:
                return helper(left.left, right.right) and helper(left.right, right.left)

        if root is None:
            return True
        else:
            return helper(root.left, root.right)

# Time complexity =  O(n) where n is the total number of nodes in the binary tree.
# Space complexity =  O(h) where h is the height of the binary tree.
