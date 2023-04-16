# medium

'''
You are given an integer array coins representing coins of different denominations and 
an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:     
        
        def helper(rem, data):
            
            if rem < 0:
                return inf
            if rem == 0:
                return 0
            if rem in data:
                return data[rem]

            data[rem] = min(helper(rem - i, data) + 1 for i in coins)
            return data[rem]
        
        ans = helper(amount, {})
        
        return -1 if ans == inf else ans

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        count, prev = 0, 1 << amount
        
        while prev & 1 == 0:
            curr = prev
            for coin in coins:
                curr |= prev >> coin
                
            if curr == prev:
                return -1
                
            count += 1
            prev = curr

        return count