#https://leetcode.com/problems/remove-k-digits/description/
#O(N),O(N)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==k:
            return "0"
        stack=[]

        for digit in num:
            #when top element of stack is greater than curr digit and we still have deletions left to make
            while stack and k>0 and stack[-1]>digit:
                stack.pop()
                k-=1
            stack.append(digit)

        #if we still need ro rem elements rem from end
        if k>0:
            stack=stack[:-k]

        result="".join(stack).lstrip("0")

        return result if result else "0"
