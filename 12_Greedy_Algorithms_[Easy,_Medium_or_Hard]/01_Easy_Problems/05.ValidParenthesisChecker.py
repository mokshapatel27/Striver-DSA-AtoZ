#https://leetcode.com/problems/valid-parenthesis-string/description/

class Solution:
    def checkValidString(self, s: str) -> bool:
        maxopen=0
        minopen=0

        for char in s:
            #If we see '(', both minimum and maximum open bracket counts increase by 1
            if char=='(':
                minopen+=1
                maxopen+=1
                #If we see ')', both minimum and maximum open bracket counts decrease by 1
            elif char==')':
                minopen-=1
                maxopen-=1
                #If we see '*':
            # - min_open decreases by 1 (treating '*' as ')' to minimize open brackets)
            # - max_open increases by 1 (treating '*' as '(' to maximize open brackets)
            else:
                minopen-=1
                maxopen+=1
            #If max_open < 0, even in the best-case scenario (treating all '*' as '('),
            # we have too many ')' brackets. The string is immediately invalid!
            if maxopen<0:
                return False
            #Open count can never truly be negative. If min_open < 0, 
            # it just means we treated a '*' as ')' when we should have treated it as empty "".
            # Reset min_open back to 0.
            if minopen < 0:
                minopen=0
        return minopen==0
