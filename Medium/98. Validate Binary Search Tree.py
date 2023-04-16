# medium

'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

# https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Dfs
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, min = None, max = None):
            if not root:
                return True
            if min != None and root.val <= min:
                return False
            if max != None and root.val >= max:
                return False
            
            return dfs(root.left, min, root.val) and dfs(root.right, root.val, max)

        return dfs(root)

# Time complexity = O(n)
# Space complexity = O(2 ^ n)