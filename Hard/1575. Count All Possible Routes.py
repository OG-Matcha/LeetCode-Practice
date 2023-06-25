# hard

'''
You are given an array of distinct positive integers locations where locations[i] represents the position of city i. You are also given integers start, finish and fuel representing the starting city, ending city, and the initial amount of fuel you have, respectively.

At each step, if you are at city i, you can pick any city j such that j != i and 0 <= j < locations.length and move to city j. Moving from city i to city j reduces the amount of fuel you have by |locations[i] - locations[j]|. Please notice that |x| denotes the absolute value of x.

Notice that fuel cannot become negative at any point in time, and that you are allowed to visit any city more than once (including start and finish).

Return the count of all possible routes from start to finish. Since the answer may be too large, return it modulo 10^9 + 7.
'''

# https://leetcode.com/problems/count-all-possible-routes/description/

''' Logical Thinking
In the approach we create a 2D-array dp, where dp[i][j] contains the number of possible routes starting from the city i with j fuel. Our answer would be dp[start][fuel]. The value of dp[i][j] would be initialized with 1 if i == finish (staying at i is one way to reach finish), otherwise 0 as we did in the previous approach. We then move to all other cities except i. For each city k, we reduce the fuel by |locations[i] - locations[k]| and add the ways to reach finish from k using j - |locations[i] - locations[k]| to dp[i][j]. The state transition would be as follows:

dp[i][j] = (dp[i][j] + dp[k][j - |locations[i] - locations[k]|]) % 1000000007

The transition indicates that three nested loops are required to fill the dp array. The first loop controls the fuel and will go from j = 0 to fuel, the second loop controls the start city and runs from i = 0 to n - 1, and the third loops from k = 0 to n - 1 to cover all the cities we move to from the city i. To compute dp[i][j], we must know the values for fuel less than j because we are decrementing the fuel in its computation while moving to other cities. As a result, the outer loop must control the fuel as we progress from a lower amount of fuel to a higher amount of fuel in a bottom-up manner.
'''


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[0] * (fuel + 1) for _ in range(n)]

        for i in range(fuel + 1):
            dp[finish][i] = 1

        for j in range(fuel + 1):
            for i in range(n):
                for k in range(n):
                    if k == i:
                        continue
                    if abs(locations[i] - locations[k]) <= j:
                        dp[i][j] = (dp[i][j] + dp[k][j - abs(
                            locations[i] - locations[k])]) % 1000000007

        return dp[start][fuel]

# Time complexity = O(n^2 * fuel) where n is the length of locations
# Space complexity = O(n * fuel)
