# medium

'''
You have n bags numbered from 0 to n - 1. 
You are given two 0-indexed integer arrays capacity and rocks. 
The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks. 
You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.

Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.
'''

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        result = []
        count = 0
        
        for i in range(len(capacity)):
            result.append((capacity[i] - rocks[i]))
            
        if additionalRocks >= sum(result):
                return len(capacity)
        
        result.sort()
        
        i = 0
        while additionalRocks >= 0:
            additionalRocks -= result[i]
            count += 1
            i += 1
                
        return count - 1

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = [x - y for x, y in zip(capacity, rocks)]
        diff.sort()
        ans = 0 
        for x in diff: 
            if x <= additionalRocks: 
                ans += 1
                additionalRocks -= x
        return ans 