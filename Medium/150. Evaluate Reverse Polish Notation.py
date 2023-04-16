# medium

'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. 
That means the expression would always evaluate to a result, 
and there will not be any division by zero operation.
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack, total = [], 0

        for i in tokens:
            if i not in "+*/-":
                stack.append(int(i))
            else:
                total, left, right = 0, stack.pop(), stack.pop()

                if i == "+":
                    total += left + right

                elif i == "-":
                    total += right - left

                elif i == "*":
                    total += right * left

                else:
                    total += int(right / left)

                stack.append(total)

        return stack[-1]