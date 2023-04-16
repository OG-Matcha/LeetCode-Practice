# medium

'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''

# Brute-force
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        for _ in range(k):
            ans = nums.pop(nums.index(max(nums)))
        
        return ans

# Sort
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        return sorted(nums)[-k]

# Heap
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = nums[:k]
        heapq.heapify(heap)
        for i in nums[k:]:
            heapq.heappushpop(heap,i)
            
        return heap[0]
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        return heapq.nlargest(k, nums)[-1]

# Quick select
class Solution:
    def findKthLargest(self, nums, k):
        
        if not nums: 
            return
        
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]