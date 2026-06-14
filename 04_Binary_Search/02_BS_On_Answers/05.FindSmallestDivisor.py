#https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/submissions/2031645721/

from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        
        while low < high:
            mid = (low + high) // 2
            
            # Fast, inline ceil division sum
            total = sum((x + mid - 1) // mid for x in nums)
            
            if total <= threshold:
                high = mid      # mid could be the answer, look left
            else:
                low = mid + 1   # mid is too small, look right
                
        return low
