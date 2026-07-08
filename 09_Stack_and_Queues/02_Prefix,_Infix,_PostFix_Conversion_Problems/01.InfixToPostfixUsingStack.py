#https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1

class Solution:
    def infixtoPostfix(self, s):
        # Precedence map: higher value means higher precedence
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        #holds operators and opening brackets
        stack=[]
        #holds final results
        result=[]
        
        for char in s:
            #if it is alphabet or number never goes to st directly to res
            if char.isalnum():
                result.append(char)
            elif char=="(":
                stack.append(char)
            elif char==")":
                while stack and stack[-1]!="(":
                    #pop all operators from st and add to result
                    result.append(stack.pop())
                #pop (
                stack.pop()
            #operators case
            else:
                '''stack[-1] != '(': We stop checking if we hit a (, because operators inside brackets shouldn't bleed out.

precedence[stack[-1]] > precedence[char]: Pops operators on the stack that have strictly higher priority (e.g., popping * if the current operator is +).

precedence[stack[-1]] == precedence[char] and char != '^': Handles associativity. Left-to-right associative operators (+, -, *, /) will pop an equal-precedence operator. However, ^ evaluates right-to-left, so a current ^ will not pop an existing ^ from the stack.'''
                while stack and stack[-1]!="(" and (
                    precedence[stack[-1]]>precedence[char] or
                    (precedence[stack[-1]]==precedence[char] and char!="^")
                    ):
                        result.append(stack.pop())
                stack.append(char)
                
        
        while stack:
            result.append(stack.pop())
        return "".join(result)
