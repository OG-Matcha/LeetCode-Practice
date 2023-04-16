# meduim

'''
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
'''

# https://leetcode.com/problems/top-k-frequent-words/

# Counter & Sort
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = Counter(words)
        res = sorted(count, key=lambda word: (-count[word], word))
        return res[:k]