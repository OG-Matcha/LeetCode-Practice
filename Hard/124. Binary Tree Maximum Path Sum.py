# hard

'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''

# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Good Explanation
# https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/603423/python-recursion-stack-thinking-process-diagram/?orderBy=most_votes


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maxi = -inf

        def helper(root):
            if not root:
                return 0
            
            left_max = max(helper(root.left), 0)
            right_max = max(helper(root.right), 0)

            curr_max = root.val + left_max + right_max
            self.maxi = max(self.maxi, curr_max)

            return root.val + max(left_max, right_max)
        
        helper(root)
        return self.maxi

# Time complexity = O(n)
# Space complexity = O(n)