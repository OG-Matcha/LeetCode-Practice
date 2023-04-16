# easy

'''
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
'''

# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Dfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def dfs(root):
            if not root:
                return False
            if root.val in res:
                return True
            res.add(k - root.val)
            return dfs(root.left) or dfs(root.right)
        
        res = set()
        return dfs(root)

# Time complexity = O(n)
# Space complexity = O(n)

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        q = [root]
        seen = set()
        
        while q:
            n = q.pop(0)
            if n.val in seen:
                return True
            seen.add(k - n.val)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
                
        return False