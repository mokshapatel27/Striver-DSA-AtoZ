#https://www.geeksforgeeks.org/problems/postfix-to-infix-conversion/1

class Solution:
    def postToInfix(self, postfix):
        stack = []
        
        # Set of operators for fast lookup
        operators = set(['+', '-', '*', '/', '^'])
        
        for char in postfix:
            if char in operators:
                op2=stack.pop()
                op1=stack.pop()
                new=f"({op1}{char}{op2})"
                stack.append(new)
            else:
                stack.append(char)
        return stack[0]
