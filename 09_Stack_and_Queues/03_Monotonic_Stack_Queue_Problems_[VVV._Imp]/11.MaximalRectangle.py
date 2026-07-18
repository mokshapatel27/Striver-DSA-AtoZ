#https://leetcode.com/problems/maximal-rectangle/description/
#LEFT

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * (cols + 1) # Extra 0 at the end flushes the stack
        max_area = 0
        
        for row in matrix:
            # Step 1: Update the histogram heights for the current row
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0 # Ground level resets if we hit a '0'
            
            # Step 2: Calculate max rectangle in the current histogram using a monotonic stack
            stack = []
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
        return max_area
