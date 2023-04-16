# medium

'''
Given an integer array nums of size n, 
return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.
'''

# Sort & median
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        n = len(nums)
        mid = sorted(nums)[n // 2]
        res = sum(abs(i - mid) for i in nums)
        
        return res

# Time complexity = O(NlogN)
# Space complexity = O(1)

# Statistics module
import statistics
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        mid = int(statistics.median(nums))
        
        return sum(abs(i - mid) for i in nums)