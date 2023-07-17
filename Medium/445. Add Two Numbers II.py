# medium

'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        stack_1 = []
        stack_2 = []
        res = ListNode()

        while l1:
            stack_1.append(l1.val)
            l1 = l1.next

        while l2:
            stack_2.append(l2.val)
            l2 = l2.next

        carry = 0
        curr = 0

        while stack_1 or stack_2:

            if stack_1:
                curr += stack_1.pop()
            if stack_2:
                curr += stack_2.pop()

            res.val = curr % 10
            carry = curr // 10

            node = ListNode(carry, res)
            res = node
            curr = carry

        return res if carry else res.next

# Time complexity = O(m + n) where m and n are the number of nodes in l1 and l2
# Time complexity = O(m + n)
