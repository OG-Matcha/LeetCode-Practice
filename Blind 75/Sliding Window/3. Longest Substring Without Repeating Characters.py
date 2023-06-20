# medium

'''
Given a string s, find the length of the longest substring without repeating characters.
'''

# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        left = 0
        res = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[r])
            res = max(res, r - l + 1)

        return res

# Time complexity = O(n) where n is the length of s
# Space complexity = O(n)
