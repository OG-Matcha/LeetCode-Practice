# medium

'''
You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.
'''

# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/

# Counter & Greedy
import collections


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = collections.Counter(tasks)
        res = 0

        for i in freq.values():
            if i == 1:
                return -1
            elif i == 2:
                res += 1
            else:
                res += ceil(i / 3)

        return res


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = collections.Counter(tasks).values()
        return -1 if 1 in freq else sum((i + 2) // 3 for i in freq.values())

# Time comeplexity = O(n)
# Space comeplexity = O(n)
