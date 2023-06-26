# medium

'''
You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.
'''

# https://leetcode.com/problems/total-cost-to-hire-k-workers/description/

import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        head = costs[:candidates]
        tail = costs[max(candidates, len(costs) - candidates):]

        heapq.heapify(head)
        heapq.heapify(tail)

        ans = 0
        next_head = candidates
        next_tail = len(costs) - candidates - 1

        for _ in range(k):
            if not tail or head and head[0] <= tail[0]:
                ans += heapq.heappop(head)
                if next_head <= next_tail:
                    heapq.heappush(head, costs[next_head])
                    next_head += 1
            else:
                ans += heapq.heappop(tail)

                if next_head <= next_tail:
                    heapq.heappush(tail, costs[next_tail])
                    next_tail -= 1

        return ans

# Time complexity = O(m + klogm) where m is the given integer candidates
# Space Complexity = O(m)
