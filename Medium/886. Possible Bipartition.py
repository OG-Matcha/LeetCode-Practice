# medium

'''
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.
'''

# https://leetcode.com/problems/possible-bipartition/description/

# Dfs & Defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n == 1 or not dislikes:
            return True

        def helper(person, color):
            color_table[person] = color

            for other in dislike_table[person]:
                if color_table[other] == color:
                    return False
                if color_table[other] == 0 and not helper(other, -color):
                    return False
            return True

        dislike_table = defaultdict(list)
        color_table = defaultdict(int)

        for a, b in dislikes:
            dislike_table[a].append(b)
            dislike_table[b].append(a)
        
        for person in range(1, n + 1):
            if color_table[person] == 0 and not helper(person, 1):
                return False
        
        return True

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n == 1 or not dislikes:
            return True

        def helper(person, color, seen):
            if person in seen:
                return seen[person] == color
            
            seen[person] = color

            for other in dislike_table[person]:
                if not helper(other, -color, seen):
                    return False
            return True

        dislike_table = defaultdict(list)

        for a, b in dislikes:
            dislike_table[a].append(b)
            dislike_table[b].append(a)
        
        seen = dict()

        for person in range(1, n + 1):
            if person not in seen and not helper(person, 1, seen):
                return False
        
        return True