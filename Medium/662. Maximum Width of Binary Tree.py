# medium

'''
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.
'''

# https://leetcode.com/problems/maximum-width-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Bfs

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 0)])
        maxi = 0

        while q:
            length = len(q)
            _, start = q[0]

            for i in range(length):
                node, idx = q.popleft()

                if node.left:
                    q.append((node.left, 2 * idx))

                if node.right:
                    q.append((node.right, 2 * idx + 1))

            maxi = max(maxi, idx - start + 1)

        return maxi

# Time complexity = O(n) where n is the nubmer of nodes in the tree
# Space complexity = O(n)
