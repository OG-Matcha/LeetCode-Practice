# medium

'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
'''

# https://leetcode.com/problems/odd-even-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        first = end = head
        count = 1

        if not head:
            return head

        while end.next:
            end = end.next
            count += 1

        if count == 2:
            return head

        for _ in range(count // 2):
            curr = first.next
            first.next = first.next.next
            end.next = ListNode(curr.val)
            end = end.next
            first = first.next

        return head

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        odd = head
        even = head.next
        e_head = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = e_head

        return head
# Time complexity = O(n)
# Space complexity = O(1) 

