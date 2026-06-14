#https://leetcode.com/problems/koko-eating-bananas/

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Define the search space for Koko's speed
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            # Calculate total hours needed at speed 'mid'
            # math.ceil(p // mid) is equivalent to (p + mid - 1) // mid
            total_hours = sum((p + mid - 1) // mid for p in piles)
            
            if total_hours <= h:
                # 'mid' is feasible; try to find a smaller valid speed
                right = mid
            else:
                # 'mid' is too slow; we must increase the speed
                left = mid + 1
                
        return left
