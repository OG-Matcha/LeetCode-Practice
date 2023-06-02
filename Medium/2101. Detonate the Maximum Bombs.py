# medium

'''
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.
'''

# https://leetcode.com/problems/detonate-the-maximum-bombs/description/

from collections import defaultdict

# Dfs


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        total = len(bombs)
        data = defaultdict(list)

        for i in range(total):
            for j in range(total):
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    data[i].append(j)

        def dfs(i):
            stack = [i]
            seen = set([i])

            while stack:
                curr = stack.pop()

                for n in data[curr]:
                    if n not in seen:
                        seen.add(n)
                        stack.append(n)

            return len(seen)

        ans = 0
        for i in range(total):
            ans = max(ans, dfs(i))

        return ans


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        total = len(bombs)
        data = defaultdict(list)

        for i in range(total):
            for j in range(total):
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    data[i].append(j)

        def dfs(curr, seen):
            seen.add(curr)

            for n in data[curr]:
                if n not in seen:
                    dfs(n, seen)

            return len(seen)

        ans = 0
        for i in range(total):
            seen = set()
            ans = max(ans, dfs(i, seen))

        return ans

# Time complexity = O(n^3)
# Space complexity = O(n^2)
