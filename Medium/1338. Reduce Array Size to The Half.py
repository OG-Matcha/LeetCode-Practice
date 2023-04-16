# medium

'''
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.
'''

# https://leetcode.com/problems/reduce-array-size-to-the-half/

# Hash map & Counting sort
from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        length = len(arr)
        count = Counter(arr)
        
        counting = [0] * (length + 1)
        for freq in count.values():
            counting[freq] += 1
            
        ans, removed, half, freq = 0, 0, length // 2, length
        
        while removed < half:
            ans += 1
            
            while counting[freq] == 0:
                freq -= 1
            
            removed += freq
            counting[freq] -= 1
        
        return ans

# Time complexity = O(n)
# Space complexity = O(n)

# Hash map & Sorting
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        freq = list(count.values())
        freq.sort()
        
        ans, removed, half = 0, 0, len(arr) // 2
        
        while removed < half:
            ans += 1
            removed += freq.pop()

        return ans

# Time complexity = O(nlogn)
# Space complexity = O(n)