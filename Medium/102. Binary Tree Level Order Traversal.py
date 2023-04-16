# medium

'''
Given the root of a binary tree, 
return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''

# Deque & bfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        deque = collections.deque([root])
        
        while deque:
            
            curr = []

            for _ in range(len(deque)):
                
                node = deque.popleft()
                
                if node:
                    
                    curr.append(node.val)
                    
                    if node.left:
                        deque.append(node.left)
                    if node.right:
                        deque.append(node.right)
            
            if curr:
                res.append(curr)
        
        return res

# Time complexity = O(n)
# Space complexity = O(n)

# List comprehension
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans, level = [], [root]
        
        while root and level:
            ans.append([node.val for node in level])            
            level = [kid for n in level for kid in (n.left, n.right) if kid]
            
        return ans