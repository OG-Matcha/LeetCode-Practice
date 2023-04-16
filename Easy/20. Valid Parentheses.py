# easy

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesPair = {')':'(', ']':'[', '}':'{'}
        stack = []
        index = 0
        balanced = True
        while index < len(s) and balanced:
            char = s[index]
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if len(stack) == 0:
                    balanced = False
                    break
                elif parenthesesPair[char] == stack[-1]:
                    stack.pop()
                else:
                    balanced = False
            index += 1
        if len(stack) == 0 and balanced == True:
            return True
        else:
            return False