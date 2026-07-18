#https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #append a 0 to automatically flush out remaning bars in the stack at the end
        heights.append(0)
        stack=[]
        maxar=0

        for i,h in enumerate(heights):
            #if height of bar at top of the stack is strictly >than our current bars height
            while stack and stack[-1][1]>h:
                #pop the bar of which area is being calculated
                pop_idx,pop_h=stack.pop()

                width=i if not stack else (i-stack[-1][0]-1)

                maxar=max(maxar,pop_h*width)
            stack.append((i,h))
        return maxar

