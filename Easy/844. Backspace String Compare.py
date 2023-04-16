# easy

'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def stack(string):
            stack = []
            for i in string:
                if i == "#":
                    if not(stack):
                        continue
                    stack.pop()
                else:
                    stack.append(i)
            return stack
                
        return stack(s) == stack(t)