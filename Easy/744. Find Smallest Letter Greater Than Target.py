# easy

'''
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
'''

# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

import bisect


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return letters[left % len(letters)]


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = bisect.bisect_right(letters, target)
        return letters[idx % len(letters)]

# Time complexity = O(logn) where n is the number of characters in letters
# Time complexity = O(1)
