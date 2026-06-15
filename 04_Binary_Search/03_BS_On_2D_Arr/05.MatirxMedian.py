#https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1

import sys
from bisect import bisect_right

class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        # The median must have exactly this many elements smaller than or equal to it
        required_smaller_or_equal = (n * m) // 2
        
        # Define the search space based on the matrix constraints or actual boundaries
        low = min(mat[i][0] for i in range(n))
        high = max(mat[i][-1] for i in range(n))
        
        ans = low
        
        # Binary search on the answer range
        while low <= high:
            mid = (low + high) // 2
            
            # Count how many elements in the entire matrix are <= mid
            # bisect_right finds the number of elements <= mid in a sorted row
            count = sum(bisect_right(row, mid) for row in mat)
            
            if count > required_smaller_or_equal:
                ans = mid       # mid could be a candidate for median
                high = mid - 1  # Try to find a smaller valid value
            else:
                low = mid + 1   # mid is too small, move right
                
        return ans
