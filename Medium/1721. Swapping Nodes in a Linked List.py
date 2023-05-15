# medium

'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
'''

# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Two Pointers


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = head
        fast = head

        for _ in range(k - 1):
            fast = fast.next

        left = fast

        while fast.next:
            slow = slow.next
            fast = fast.next

        left.val, slow.val = slow.val, left.val

        return head

# Time complexity = O(n) where n is the length of the linkedlist, exactly 2n - k
# Space complexity = O(1)
