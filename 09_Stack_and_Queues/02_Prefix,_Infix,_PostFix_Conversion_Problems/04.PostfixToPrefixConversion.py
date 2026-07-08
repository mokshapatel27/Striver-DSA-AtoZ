#https://www.geeksforgeeks.org/problems/postfix-to-prefix-conversion/1

class Solution:
    def postToPre(self, s):
        stack=[]
        
        for char in s:
            if char in "+-*/^":
                op2=stack.pop()
                op1=stack.pop()
                
                new=char+op1+op2
                stack.append(new)
            else:
                stack.append(char)
                
        return stack[0]
