# medium

'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
'''

# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(q, [nums1[i] + nums2[j], i, j])

        q = [[nums1[0] + nums2[0], 0, 0]]
        pairs = []

        while q and len(pairs) < k:
            _, i, j = heapq.heappop(q)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)

            if j == 0:
                push(i + 1, 0)

        return pairs

# Time complexity = O(min(klogk, (m * n)log(m * n))) where m and n is the length nums1 and nums2
# Space complexity = O(min(k, (m * n)))
