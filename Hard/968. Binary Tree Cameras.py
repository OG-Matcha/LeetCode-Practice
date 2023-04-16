# hard

'''
You are given the root of a binary tree. 
We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, 
and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        self.output = 0
        
        def dfs(node):
            if not node:
                return False, True
            
            c1, m1 = dfs(node.left)
            c2, m2 = dfs(node.right)
            
            camera, monitor = False, False
            
            if c1 or c2:
                monitor = True
            if not m1 or not m2:
                camera = True
                self.output += 1
                monitor = True
            
            return camera, monitor
        
        c, m = dfs(root)
        if not m:
            return self.output + 1
        
        return self.output

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        
        def dfs(root):
            
            if not root: 
                return 2
            
            l, r = dfs(root.left), dfs(root.right)
            
            if l == 0 or r == 0:
                self.res += 1
                return 1
            
            return 2 if l == 1 or r == 1 else 0
        
        return (dfs(root) == 0) + self.res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
                
            if not node:
                return 1
            
            l = dfs(node.left)
            r = dfs(node.right)

            if l == 0 or r == 0:
                self.sum += 1
                return 2
            
            elif l == 2 or r == 2:
                return 1
            
            else:
                return 0
        
        self.sum = 0
        
        if dfs(root) == 0:
            self.sum += 1
        
        return self.sum