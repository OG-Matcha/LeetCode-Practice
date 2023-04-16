# medium
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal 
of a binary tree and inorder is the inorder traversal of the same tree, 
construct and return the binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def arr_to_tree(left, right):
            nonlocal pre_idx
            
            if left > right:
                return None
            
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            
            pre_idx += 1
            
            root.left = arr_to_tree(left, in_idx_map[root_val] - 1)
            root.right = arr_to_tree(in_idx_map[root_val] + 1, right)
            
            return root
        
        pre_idx = 0
        
        in_idx_map = {}
        for idx, val in enumerate(inorder):
            in_idx_map[val] = idx
        
        return arr_to_tree(0, len(preorder) - 1)

# Time complexity = O(n)
# Space complexity = O(n)