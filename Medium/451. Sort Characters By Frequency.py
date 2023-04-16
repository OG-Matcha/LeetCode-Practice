# medium

'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
'''

# https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        data = collections.Counter(s)
        res = ""
        for val, fre in data.most_common():
            res += val * fre

        return res

# Time complexity: O(nlogk), if we think k at most 62 characters, it can be O(n)
# Space complexity: O(n)