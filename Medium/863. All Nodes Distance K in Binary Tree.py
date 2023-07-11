# medium

'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order. 
'''

# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

# Definition for a binary tree node.


import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        data = collections.defaultdict(list)

        def build(par, chi):
            if par and chi:
                data[par.val].append(chi.val)
                data[chi.val].append(par.val)

            if chi.left:
                build(chi, chi.left)
            if chi.right:
                build(chi, chi.right)

        build(None, root)

        bfs = [target.val]
        seen = set(bfs)

        for i in range(k):
            new = []

            for q_node in bfs:
                for con_node in data[q_node]:
                    if con_node not in seen:
                        new.append(con_node)

            bfs = new
            seen |= set(bfs)

        return bfs

# Time complexity = O(n) where n is the number of node in the binary tree
# Time complexity = O(n)
