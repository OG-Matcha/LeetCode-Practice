# medium

'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

# https://leetcode.com/problems/top-k-frequent-elements/description/

import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i[0] for i in collections.Counter(nums).most_common(k)]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = collections.Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)

# Time complexity = O(nlogk) where n is the number of elements in the list, k is elements we take
# Space complexity = O(n + k)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        count = collections.Counter(nums).items()

        for num, freq in count:
            bucket[freq].append(num)

        ans = []
        idx = len(nums)

        while k > 0:
            while not bucket[idx]:
                idx -= 1

            for num in bucket[idx]:
                if k == 0:
                    break
                ans.append(num)
                k -= 1

            idx -= 1

        return ans


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        count = collections.Counter(nums).items()

        for num, freq in count:
            bucket[freq].append(num)

        lst = [item for sub in bucket for item in sub]

        return lst[::-1][:k]

# Time complexity = O(n) where n is the number of elements in the list
# Space complexity = O(n)
