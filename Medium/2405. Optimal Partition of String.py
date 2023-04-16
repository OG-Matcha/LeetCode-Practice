# medium

'''
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.
'''

# https://leetcode.com/problems/optimal-partition-of-string/description/


class Solution:
    def partitionString(self, s: str) -> int:

        seen = ""
        count = 0

        for i, v in enumerate(s):
            if v not in seen:
                seen += v
            else:
                seen = v
                count += 1

        return count + 1

# Time complexity = O(n)
# Space complexity = O(n)
