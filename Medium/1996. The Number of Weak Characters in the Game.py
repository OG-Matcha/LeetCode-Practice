# easy

'''
You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.
'''

# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

# Sort
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort(key= lambda x: (-x[0], x[1]))
        count = 0
        curr_max = 0
        
        for _, d in properties:
            if d < curr_max:
                count += 1
            else:
                curr_max = d
                
        return count

# Time complexity = O(nlogn)
# Space complexity = O(1)

# Stack
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort(key= lambda x: (x[0], -x[1]))
        count = 0
        stack = []
        
        for _, d in properties:
            while stack and stack[-1] < d:
                count += 1
                stack.pop()
            stack.append(d)
                
        return count