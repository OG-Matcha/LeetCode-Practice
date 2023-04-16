# easy

'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.
'''

# https://leetcode.com/problems/unique-number-of-occurrences/

# Hash map
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        map = {}

        for i in arr:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
        
        res = set()

        for val in map.values():
            if val in res:
                return False
            else:
                res.add(val)
        
        return True

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        map = {}

        for i in arr:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
        
        res = set(map.values())

        return len(map.keys()) == len(res)

# Time complexity = O(n)
# Space complexity = O(n)

# Counter
import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        map = collections.Counter(arr)

        res = set()

        for i in map.values():
            if i in res:
                return False
            res.add(i)

        return True

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len((map := collections.Counter(arr)).keys()) == len(set(map.values()))

# Time complexity = O(n)
# Space complexity = O(n)