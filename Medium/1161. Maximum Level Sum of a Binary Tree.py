# medium

'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
'''

# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/

import collections

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Dfs


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        data = collections.defaultdict(int)

        def dfs(root, level):
            if not root:
                return
            data[level] += root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 1)

        return max(data, key=data.get)


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        data = []

        def dfs(root, level):
            if not root:
                return
            if len(data) < level:
                data.append(root.val)
            else:
                data[level - 1] += root.val

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 1)

        return data.index(max(data)) + 1

# Time complexity = O(n)
# Space complexity = O(n)
