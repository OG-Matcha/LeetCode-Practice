# easy

'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
'''

# https://leetcode.com/problems/leaf-similar-trees/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Dfs
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        val1 = []
        val2 = []

        def dfs(root, res):
            if not root.left and not root.right:
                res.append(root.val)
            if root.left:
                dfs(root.left, res)
            if root.right:
                dfs(root.right, res)
        
        dfs(root1, val1)
        dfs(root2, val2)

        return val1 == val2

# Time complexity = O(n)
# Space complexity = O(n)

# Dfs & Generator
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    
        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                yield root.val
                return

            yield from dfs(root.left)
            yield from dfs(root.right)

        return all(a == b for a, b in itertools.zip_longest(dfs(root1), dfs(root2)))
    
# Time complexity = O(n)
# Space complexity = O(h)