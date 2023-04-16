# medium

'''
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
'''

# https://leetcode.com/problems/removing-stars-from-a-string/description/

# Stack


class Solution:
    def removeStars(self, s: str) -> str:

        stack = []

        for i in s:
            if i == "*":
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)

# Time complexity = O(n)
# Space complexity = O(n)
