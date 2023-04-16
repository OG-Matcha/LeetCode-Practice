# easy

'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.
'''

# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Dfs


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        self.res = []

        def dfs(root):
            if not root:
                return

            self.res.append(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return self.res

# Time complexity = O(n)
# Space complexity = O(1)
