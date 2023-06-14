# easy

'''
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
'''

# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DfS


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        data = []

        def dfs(root):
            if not root:
                return
            data.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        mini = float("inf")
        data.sort()

        for i in range(1, len(data)):
            mini = min(mini, data[i] - data[i - 1])

        return mini

# Time complexity = O(nlogn) where n is the number of nodes
# Space complexity = O(n)

# Inorder Traversal


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        data = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            data.append(root.val)
            inorder(root.right)

        inorder(root)

        mini = float("inf")

        for i in range(1, len(data)):
            mini = min(mini, data[i] - data[i - 1])

        return mini


# Time complexity = O(n)
# Space complexity = O(n)

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.mini = float("inf")

        def inorder(root):
            if not root:
                return

            inorder(root.left)

            if self.prev is not None:
                self.mini = min(self.mini, root.val - self.prev)

            self.prev = root.val
            inorder(root.right)

        inorder(root)

        return self.mini

# Time complexity = O(n)
# Space complexity = O(1) or O(h) where h is the height of BST if we consider stack calls
