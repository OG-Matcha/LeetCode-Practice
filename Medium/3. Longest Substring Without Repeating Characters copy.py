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

            seen.add(s[right])
            res = max(res, right - left + 1)

        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = dict()
        left = 0
        res = 0

        for right in range(len(s)):
            curr = s[right]
            if curr in seen and seen[curr] >= left:
                left = seen[curr] + 1
            else:
                res = max(res, right - left + 1)
            seen[curr] = right

        return res

# Time complexity = O(n) where n is the length of s
# Space complexity = O(n)
