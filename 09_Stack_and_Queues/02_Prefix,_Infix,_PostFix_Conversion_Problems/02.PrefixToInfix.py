#https://www.geeksforgeeks.org/problems/prefix-to-infix-conversion/1

class Solution:
    def preToInfix(self, pre_exp):
        operators = set(['+', '-', '*', '/', '%', '^'])
        stack=[]
        
        #ensures that we process operands before their corresponding operators.
        for char in reversed(pre_exp):
            if char in operators:
                #1st element left hand operand 2nd element right hand
                op1=stack.pop()
                op2=stack.pop()
                
                newexp=f"({op1}{char}{op2})"
                stack.append(newexp)
            else:
                stack.append(char)
        return stack[0]
