# hard

'''
You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble. You are also given the integer k.

Divide the marbles into the k bags according to the following rules:

No bag is empty.
If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
If a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].
The score after distributing the marbles is the sum of the costs of all the k bags.

Return the difference between the maximum and minimum scores among marble distributions.
'''

# https://leetcode.com/problems/put-marbles-in-bags/description/

''' Logical Thinking
All of our bags are continuous slices of the array and all marbles must be in a bag and all bags are nonempty, so we're constructing a partition of the array with k slices and summing the first and last element of each slice.

No matter what, the first element of the array will count in the first slice and the last element of the array will count in the last slice.

Otherwise, we can think of our k slices as adding k - 1 separators to the array, where a separators is placed between index i and index i + 1 and adds the value at both indices to the overall score (since the former will be the last element of the previous slice and the latter will be the last element of the next one). The maximal partition will use the k - 1 separators that have the largest sum and the minimal solution will use the k - 1 separators that have the smallest sum.

Find the value of each separator, sort them, and take the largest k - 1 and subtract the smallest k - 1. We don't have to care about the value of the first index and the value of the last index, since they are present in both the maximal and minimal partition.
'''


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        pairs = sorted(weights[i] + weights[i + 1]
                       for i in range(len(weights) - 1))
        ans = 0

        for i in range(k - 1):
            ans += pairs[len(weights) - 2 - i] - pairs[i]

        return ans

# Time complexity = O(nlogn) where n is the length of weights
# Time complexity = O(n)
