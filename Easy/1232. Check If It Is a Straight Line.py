# easy

'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
'''

# https://leetcode.com/problems/check-if-it-is-a-straight-line/description/


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        x = coordinates[1][0] - coordinates[0][0]
        y = coordinates[1][1] - coordinates[0][1]

        for xi, yi in coordinates:
            if (xi - coordinates[0][0]) * y != (yi - coordinates[0][1]) * x:
                return False

        return True

# Time complexity = O(n)
# Space complexity = O(1)
