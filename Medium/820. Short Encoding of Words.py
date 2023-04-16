# medium

'''
A valid encoding of an array of words is any reference string s and array of indices indices such that:

• words.length == indices.length
• The reference string s ends with the '#' character.
• For each index indices[i], the substring of s starting from indices[i] 
  and up to (but not including) the next '#' character is equal to words[i].

Given an array of words, return the length of the shortest 
reference string s possible of any valid encoding of words.
'''

# Store prefixes
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        check = set(words)
        
        for w in words:
            for i in range(1, len(w)):
                check.discard(w[i:])

        return sum(len(w) + 1 for w in check)

# Time Complexity: O(∑w_i^2), where w_i is the length of words[i].
# Space Complexity: O(∑w_i), the space used in storing suffixes.

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(words, key=len, reverse=True)
        handled = set()
        result = 0
        
        for w in words:
            if w not in handled:
                result += len(w)
                result += 1
                for i in range(len(w)):
                    substring = w[i:]
                    handled.add(substring)
        
        return result