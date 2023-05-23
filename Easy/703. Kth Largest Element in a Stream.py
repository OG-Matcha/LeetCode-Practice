# easy

'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
'''

# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(nums)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]

# Time complexity = O(nlogn + mlogk) where n is the length of nums and m is the number of calls to add()
# Space complexity = O(n)


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]

# Time complexity: O(nlogk + mlogk) where n is the length of nums and m is the number of calls to add()
# Space complexity: O(k)
