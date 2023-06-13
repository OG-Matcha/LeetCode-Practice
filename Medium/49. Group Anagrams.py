# medium

'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

# https://leetcode.com/problems/group-anagrams/description/

import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        data = collections.defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord("a")] += 1

            data[tuple(count)].append(word)

        return data.values()

# Time complexity = O(n) where n is the length of strs
# Space complexity = O(n)
