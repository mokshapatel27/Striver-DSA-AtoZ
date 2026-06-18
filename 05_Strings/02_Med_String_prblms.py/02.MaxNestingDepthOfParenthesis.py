#https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

class Solution:
    def maxDepth(self, s: str) -> int:
        maxd=0
        currd=0

        for char in s:
            if char=='(':
                currd+=1
                if currd>maxd:
                    maxd=currd
            elif char==')':
                currd-=1
        return maxd
