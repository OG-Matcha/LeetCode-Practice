# medium

'''
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
'''

# https://leetcode.com/problems/minimum-penalty-for-a-shop/description/


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        res = 0
        curr = 0
        mini = 0

        for i, v in enumerate(customers):
            if v == 'Y':
                curr -= 1
            else:
                curr += 1

            if curr < mini:
                mini = curr
                res = i + 1

        return res

# Time complexity = O(n) where n is the number of customers
# Space complexity = O(1)
