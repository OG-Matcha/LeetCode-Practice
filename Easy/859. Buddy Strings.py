# easy

'''
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
'''

# https://leetcode.com/problems/buddy-strings/description/


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        if s == goal and len(set(s)) < len(s):
            return True

        data = []

        for a, b in zip(s, goal):
            if a != b:
                data.append((a, b))

        return len(data) == 2 and data[0] == data[1][::-1]

# Time complexity = O(n) where n is the length of s
# Time complexity = O(n)
