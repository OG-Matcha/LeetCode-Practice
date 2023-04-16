# medium

'''
Given the root of a binary tree, return the sum of values of its deepest leaves.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        prev, curr = [], [root]

        while curr:

            temp = []

            for n in curr:

                if n.left:
                    temp.append(n.left)

                if n.right:
                    temp.append(n.right)

            prev, curr = curr, temp
      
        return sum(i.val for i in prev)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        tree = [root]

        while tree:

            temp = []
            temp_sum = 0

            for node in tree:

                temp_sum += node.val

                if node.left:
                    temp.append(node.left)

                if node.right:
                    temp.append(node.right)

            tree = temp
            
        return temp_sum
