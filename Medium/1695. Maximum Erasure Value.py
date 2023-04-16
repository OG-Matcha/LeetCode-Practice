# medium

'''
You are given an array of positive integers nums and want to erase a subarray containing unique elements. 
The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, 
if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
'''

# Hash table & Sliding window

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        left = 0
        right = 0
        maxi = 0
        ans = 0
        length = len(nums)
        exist = set()
        
        while left < length and right < length:
            
            if nums[right] not in exist:
                exist.add(nums[right])
                ans += nums[right]
                right += 1
                maxi = max(maxi, ans)
            
            else:
                exist.remove(nums[left])
                ans -= nums[left]
                left += 1
        
        return maxi

# Hash table & Queue

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        q = deque()
        exist = set()
        curr_sum = 0
        maxi = 0
        
        for num in nums:
            
            if num not in exist:
                q.append(num)
                exist.add(num)
                curr_sum += num
                
            else:
                while q[0] != num:
                    pop = q.popleft()
                    exist.discard(pop)
                    curr_sum -= pop
                pop = q.popleft()
                q.append(num)
                    
            if curr_sum > maxi:
                maxi = curr_sum
                
        return maxi