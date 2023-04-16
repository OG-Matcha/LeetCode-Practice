# medium

'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Two pointer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        start = end = head
        
        for _ in range(n):
            end = end.next
        
        if not end:
            return head.next
        
        while end.next:
            start = start.next
            end = end.next
        
        start.next = start.next.next
        
        return head

# Time Complexity : O(N), where, N is the number of nodes in the given list. Although, the time complexity is same as above solution, we have reduced the constant factor in it to half.
# Space Complexity : O(1), since only constant space is used.