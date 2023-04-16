# medium

'''
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.
'''

# https://leetcode.com/problems/linked-list-random-node/description/

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.data = []
        while head:
            self.data.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return self.data[int(random.random() * len(self.data))]

# Time complexity = O(n)
# Space complexity = O(n)
