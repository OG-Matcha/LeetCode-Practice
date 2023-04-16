# easy

"""
You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

abc
bce
cae
You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.
"""

# https://leetcode.com/problems/delete-columns-to-make-sorted/description/

# Iterative
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        m = len(strs)
        res = 0

        for i in range(n):
            for j in range(1, m):
                if strs[j][i] < strs[j - 1][i]:
                    res += 1
                    break

        return res


# Time complexity = O(n * m)
# Space complexity = O(1)
