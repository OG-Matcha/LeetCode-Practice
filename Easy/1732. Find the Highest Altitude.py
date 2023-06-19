# easy

'''
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
'''

# https://leetcode.com/problems/find-the-highest-altitude/description/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi = 0
        curr = 0
        
        for i in gain:
            curr += i
            maxi = max(maxi, curr)
        
        return maxi

# Time complexity = O(n) where n is the length of gain
# Space complexity = O(1)