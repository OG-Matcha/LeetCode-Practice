# medium

'''
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
'''

# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head
        res = 0

        while fast:
            slow = slow.next
            fast = fast.next.next

        curr, prev = slow, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        start = head
        while prev:
            res = max(res, start.val + prev.val)
            prev = prev.next
            start = start.next

        return res

# Time complexity = O(n)
# Space complexity = O(1)


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []

        slow = head
        fast = head
        res = 0

        while fast:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        for i in range(len(stack) - 1, -1, -1):
            res = max(res, stack[i] + slow.val)
            slow = slow.next

        return res

# Time complexity = O(n)
# Space complexity = O(n)
