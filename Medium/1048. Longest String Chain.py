# medium

'''
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere 
in wordA without changing the order of the other characters to make it equal to wordB.

• For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, 
where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. 
A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.
'''

# Bottom-Up DP
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dp = {}
        result = 1

        for word in sorted(words, key=len):
            dp[word] = 1

            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]

                if prev in dp:
                    dp[word] = max(dp[prev] + 1, dp[word])
                    result = max(result, dp[word])

        return result

# Time: O(NlogN + N*L*L), where N <= 1000 is number of words, L <= 16 is length of a word
# Space: O(N)

# Top-Down DP
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordSet = set(words)

        @lru_cache(None)
        def dp(word):
            ans = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1:]
                if predecessor in wordSet:
                    ans = max(ans, dp(predecessor) + 1)
            return ans

        return max(dp(w) for w in words)

# Time: O(N * L * L), where N <= 1000 is number of words, L <= 16 is length of a word
# Space: O(N)

# Longest Increasing Subsequence Idea
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def isPredecessor(word1, word2):
            if len(word1) + 1 != len(word2): return False
            i = 0
            for c in word2:
                if i == len(word1): return True
                if word1[i] == c:
                    i += 1
            return i == len(word1)
        
        words.sort(key=len)
        n = len(words)
        dp = [1] * n
        ans = 1
        for i in range(1, n):
            for j in range(i):
                if isPredecessor(words[j], words[i]) and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
            ans = max(ans, dp[i])
        return ans

# Time: O(N^2 * L), where N <= 1000 is number of words, L <= 16 is length of each word.
# Space: O(N)