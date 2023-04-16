# medium

'''
You are given a string s and an integer k, 
a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, 
causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. 
It is guaranteed that the answer is unique.
'''

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # stack to store the pair[character, count]
        stack = []
        
        for char in s:
            # If the stack is not empty and last char in stack and current char are same,
            # then increment the count
            if stack and char == stack[-1][0]:
                stack[-1][1] += 1
                #if count of char == k, pop it from stack
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char,1])
        
        res = ""
        for char, count in stack:
            res += char*count
        
        return res


        