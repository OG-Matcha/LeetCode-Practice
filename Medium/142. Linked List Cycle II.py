# medium

'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
'''

# https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Hash Table


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        data = set()

        while start:
            if start in data:
                return start
            else:
                data.add(start)
                start = start.next

# Time complexity = O(n)
# Space complexity = O(n)

# Slow & Fast node


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

# Time complexity = O(n)
# Space complexity = O(1)
