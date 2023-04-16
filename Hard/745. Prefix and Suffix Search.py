# hard

'''
Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the WordFilter class:

• WordFilter(string[] words) Initializes the object with the words in the dictionary.

• f(string prefix, string suffix) Returns the index of the word in the dictionary, 
  which has the prefix prefix and the suffix suffix. If there is more than one valid index, 
  return the largest of them. If there is no such word in the dictionary, return -1.
'''

import collections

Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter:
    
    def __init__(self, words: List[str]):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight
                    
    def f(self, prefix: str, suffix: str) -> int:
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

# Time Complexity: O(NK^2 + QK) where N is the number of words, K is the maximum length of a word, and Q is the number of queries.
# Space Complexity: O(NK^2), the size of the trie.