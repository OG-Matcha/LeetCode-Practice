# medium

'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''

# https://leetcode.com/problems/course-schedule/description/

import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        data = [[] for _ in range(numCourses)]
        need = [0] * numCourses

        for i, j in prerequisites:
            data[j].append(i)
            need[i] += 1

        q = collections.deque()

        for i in range(numCourses):
            if not need[i]:
                q.append(i)

        seen = 0

        while q:
            curr = q.popleft()
            seen += 1

            for node in data[curr]:
                need[node] -= 1

                if need[node] == 0:
                    q.append(node)

        return seen == numCourses

# Time complexity = O(m + n) where n is the number of courses and m is the length of prerequisites
# Space complexity = O(m + n)
