#https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1

class Solution:
    def nthRoot(self, n: int, m: int) -> int:
        # Base cases
        if m == 0 or m == 1:
            return m
            
        low = 1
        high = m
        
        while low <= high:
            mid = (low + high) // 2
            mid_pow = mid ** n
            
            if mid_pow == m:
                return mid
            elif mid_pow > m:
                high = mid - 1
            else:
                low = mid + 1
                
        return -1
