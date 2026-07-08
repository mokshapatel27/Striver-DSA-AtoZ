#https://www.geeksforgeeks.org/problems/prefix-to-postfix-conversion/1

class Solution:
    def preToPost(self, s):
        operators = set(['+', '-', '*', '/'])
        stack=[]
        
        for char in reversed(s):
            if char in operators:
                op1=stack.pop()
                op2=stack.pop()
                
                newexp=op1+op2+char
                stack.append(newexp)
                
            else:
                stack.append(char)
        return stack[0]
