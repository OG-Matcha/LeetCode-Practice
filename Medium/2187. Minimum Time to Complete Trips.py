# medium

'''
You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.
'''


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def check(mid):
            return sum(mid // t for t in time) >= totalTrips

        left = 1
        right = totalTrips * min(time)

        while left < right:
            mid = (left + right) // 2

            if not check(mid):
                left = mid + 1
            else:
                right = mid

        return left

# Time complexity = O(nlog(k)) where k is the range of bounds
# Space complexity = O(1)
