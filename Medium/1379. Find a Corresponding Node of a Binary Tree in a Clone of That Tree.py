# medium

'''
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer 
must be a reference to a node in the cloned tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if original == target:
            return cloned
        
        elif original.left == None and original.right == None:
            return None
        
        else:
            if original.left != None:
                result_left = self.getTargetCopy(original.left, cloned.left, target)
                
                if result_left != None:
                    return result_left
            
            if original.right != None:
                result_right = self.getTargetCopy(original.right, cloned.right, target)
                
                if result_right != None:
                    return result_right
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def pre(o, c):    
            if o:
                if o == target:
                    return c
                else:
                    return pre(o.left, c.left) or pre(o.right, c.right)
                
        return pre(original,cloned)