#https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # 1. Quick sanity check
        if m * k > len(bloomDay):
            return -1
        
        # 2. Define the search space
        low, high = min(bloomDay), max(bloomDay)
        
        # 3. Binary Search
        while low < high:
            mid = (low + high) // 2
            
            # Inline feasibility check
            bouquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom <= mid:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            
            # Shrink search space
            if bouquets >= m:
                high = mid      # mid could be the answer, look left
            else:
                low = mid + 1   # mid is too small, look right
                
        return low
