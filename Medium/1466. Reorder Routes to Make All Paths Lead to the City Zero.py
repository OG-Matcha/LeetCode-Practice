# medium

'''
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.
'''

# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        res = 0
        data = defaultdict(list)
        q = deque([0])
        visited = set([0])

        for ori, des in connections:
            data[ori].append((des, 1))
            data[des].append((ori, 0))

        while q:
            curr = q.popleft()

            for node, cost in data[curr]:
                if node not in visited:
                    visited.add(node)
                    res += cost
                    q.append(node)

        return res

# Time complexity = O(n)
# Space complexity = O(n)