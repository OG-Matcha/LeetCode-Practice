# medium

'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''

# https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev, cur, ans = None, head, head.next
        while cur and cur.next:
            adj = cur.next
            if prev:
                prev.next = adj

            cur.next, adj.next = adj.next, cur
            prev, cur = cur, cur.next

        return ans

# Time complexity = O(n)
# Space complexity = O(1)
