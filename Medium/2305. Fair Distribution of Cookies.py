# medium

'''
You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.
'''

# https://leetcode.com/problems/fair-distribution-of-cookies/description/


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        def dfs(idx, maxi):

            if idx >= len(cookies):
                self.res = min(self.res, maxi)
                return

            if maxi >= self.res:
                return

            for i in range(min(idx + 1, k)):
                curr[i] += cookies[idx]
                dfs(idx + 1, max(maxi, curr[i]))
                curr[i] -= cookies[idx]

        self.res = float("inf")
        curr = [0] * k

        dfs(0, 0)

        return self.res

# Time complexity = O(k^n) where n is the length of cookies
# Time complexity = O(k + n)
