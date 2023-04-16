# easy

'''
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.

Return the number of different transformations among all words we have.
'''

# https://leetcode.com/problems/unique-morse-code-words/

# Set
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morce = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        ans = set()
        
        for i in words:
            code = ""
            for j in i:
                code += morce[ord(j) - ord("a")]
            ans.add(code)
            
        return len(ans)

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morce = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        ans = {"".join(morce[ord(c)-ord("a")] for c in word) for word in words}
        
        return len(ans)