# hard

'''
You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.
'''

# https://leetcode.com/problems/tallest-billboard/description/

''' Logical Thinking
Instead of generating all combinations by brute force, we can use a dynamic programming approach to optimize the solution. Rather than tracking rods individually and saving the state as (left, right), it's better to name them according to their height as taller and shorter. 

Let dp[diff] = taller, where diff is the difference between the two rods taller - shorter. Initially, we set dp[0] = 0 because initially, we have taller = shorter = 0. 

However, we notice that for the same height difference of 1, we can form a higher stand, so there is no need to store the combination with the shorter one.

Likewise, for the same height difference of 0, a combination with a height of 3 can be formed, making the combination with a height of 0 unnecessary.

Therefore, only the maximum height of the taller stand is stored in each dp[diff]. We won't waste time and space by saving other smaller heights. As you may have expected, dp[0] will hold the answer at the end, since dp[0] implies that the rods are the same height.

A new hashmap new_dp is created as a copy of the current hashmap dp.

If we were to skip (not use for either support) the new rod, then dp would not change. That's why we are initializing new_dp by copying dp. It implicitly considers this option.

Recall that for each state already stored in dp[diff] = taller, we can have three options
to update new_dp with a new rod of height r:

Not add r to either stand, which we have implemented already (by copying dp to new_dp).

Add r to the taller stand and create a new state diff + r with a value of taller + r, update this case in new_dp.

Add r to the shorter stand. What will the new height difference be? Add the rod's height to shorter, then use absolute value to find the difference. The new state is abs(shorter + r - taller). The value will be max(shorter + r, taller), in case adding r makes the shorter support the taller one.

Before moving on to the next rod, we let dp = new_dp.

Once the iteration over all rods is complete, we can return dp[0] as it denotes the maximum height we can reach upon maintaining a 0 height difference.
'''


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}

        for r in rods:
            new_dp = dp.copy()
            for diff, taller in dp.items():
                shorter = taller - diff

                new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)

                new_diff = abs(shorter + r - taller)
                new_taller = max(shorter + r, taller)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_taller)

            dp = new_dp

        return dp.get(0, 0)

# Time complexity = O(n * m) where n is the kength of rods and m is the maximum sum of rods
# Space complexity = O(m)
