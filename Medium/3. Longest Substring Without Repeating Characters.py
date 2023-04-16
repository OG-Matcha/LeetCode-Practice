# medium

'''
Given a string s, find the length of the longest substring without repeating characters.
'''

# Brute-force (BAD)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         ans=0
#         for i in range(len(s)):
#             for j in range(i+1,len(s)):
#                 a=s[i:j]
#                 if len(a)==len(set(a)):
#                     ans=max(len(a),ans)
#         return ans

# Sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        start = 0
        end = 0
        seen = set()
        res = 0
        
        while start < len(s) and end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                end += 1
                res = max(res, end - start)
            else:
                seen.remove(s[start])
                start += 1
        return res

# Hash and queue
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        d = set()
        e = deque()
        ans = 0

        for i in range(len(s)):
            if s[i] in d:
                ans = max(ans, len(d))
                while e[0] != s[i]:
                    d.remove(e.popleft())
                d.remove(e.popleft())
                d.add(s[i])
                e.append(s[i])
                
            else:
                d.add(s[i])
                e.append(s[i])
                ans = max(ans, len(d))
        return ans