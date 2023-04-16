# medium

'''
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
'''

# Deque & bfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        deque = collections.deque()
        
        if root:
            deque.append(root)
            
        res = []
        
        while deque:

            for _ in range(len(deque)):
                
                node = deque.popleft()
                val = node.val
                
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
                    
            res.append(val)
            
        return res