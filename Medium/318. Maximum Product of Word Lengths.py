# medium

'''
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) 
where the two words do not share common letters. If no such two words exist, return 0.
'''

# Brute-force
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        maxLen = 0
        check = True
        
        for i in words:
            for j in words:

                check = True

                for k in list(i):

                    if k in j:
                        check = False
                        break

                if check and i != j:
                    maxLen = max(maxLen, len(i) * len(j))
        
        return maxLen

# Hashset
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        
        char_set = [set()] * n
        lengths = [0] * n
        
        for i in range(n):            
            char_set[i]=set(words[i])
            lengths[i]=len(words[i])
                        
        max_val = 0

        for i in range(n):
            for j in range(i+1, n):

                if not (char_set[i] & char_set[j]):
                    max_val = max(max_val, lengths[i] * lengths[j])
        
        return max_val

# Time - O(N^2 * L) - where N is the number of words and L is the max length of the word in words. The interesect operation A & B in python has a time complexity of O(min(len(A), len(B)).
# Space - O(N) - space to store the char_set and lengths.

# Python library
class Solution:
    def maxProduct(self, words: List[str]) -> int:
         return max([len(s1) * len(s2) for s1, s2 in combinations(words, 2)  if not (set(s1) & set(s2))], default=0)

# Time - O(N^2 * L) - where N is the number of words and L is the max length of the word in words. The interesect operation A & B in python has a time complexity of O(min(len(A), len(B)).
# Space - O(1)

# Bit mask
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        
        bit_masks = [0] * n
        lengths = [0] * n
        
        for i in range(n):             
            for c in words[i]:
                bit_masks[i] |= 1 << (ord(c) - ord('a')) # set the character bit            
            
            lengths[i] = len(words[i])
                        
        max_val = 0

        for i in range(n):
            for j in range(i+1, n):
                if not (bit_masks[i] & bit_masks[j]):
                    max_val = max(max_val, lengths[i] * lengths[j])
        
        return max_val  

# Time - O(N^2) - where N is the number of words.
# Space - O(N) - space to store the char_set and lengths.