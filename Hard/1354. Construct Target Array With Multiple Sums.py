# hard

'''
You are given an array target of n integers. From a starting array arr consisting of n 1's, 
you may perform the following procedure :

• let x be the sum of all elements currently in your array.
• choose index i, such that 0 <= i < n and set the value of arr at index i to x.
• You may repeat this procedure as many times as needed.

Return true if it is possible to construct the target array from arr, otherwise, return false.
'''

import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        h = [-a for a in target]
        heapq.heapify(h)
        
        while True:
            a = -heapq.heappop(h)
            total -= a
            if a == 1 or total == 1: 
                return True
            if a < total or total == 0 or a % total == 0:
                return False
            
            a %= total
            total += a
            heapq.heappush(h, -a)