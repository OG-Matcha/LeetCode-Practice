# medium

'''
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
'''

# https://leetcode.com/problems/smallest-number-in-infinite-set/description/


class SmallestInfiniteSet:

    def __init__(self):
        self.added = []
        self.seen = set()
        self.count = 1

    def popSmallest(self) -> int:
        if self.added:
            ans = heapq.heappop(self.added)
            self.seen.remove(ans)
            return ans
        else:
            ans = self.count
            self.count += 1
        return ans

    def addBack(self, num: int) -> None:
        if num < self.count and num not in self.seen:
            heapq.heappush(self.added, num)
            self.seen.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

# Time complexity = O((m + n) logn) where m is the times we called popSamllest() and n is the times we called addBack() and logn is for pushing and removing element from min-heap
# Space complexity = O(n) where n is the number of elements added to the hash set and min-heap
