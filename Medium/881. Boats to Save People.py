# medium

'''
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
'''

# https://leetcode.com/problems/boats-to-save-people/description/

# Two Pointer


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        res = 0
        i = 0
        j = len(people) - 1

        while i <= j:
            res += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1

        return res

# Time complexity = O(nlogn) where n is the number of people
# Space complexity = O(n) where n is the number of people
