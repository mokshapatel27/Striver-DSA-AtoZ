#https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1

class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0]) if n > 0 else 0
        
        max_1s_row = -1
        max_1s_count = 0
        
        for i in range(n):
            # Binary search to find the first occurrence of 1 in the current row
            low, high = 0, m - 1
            first_one_index = m  # Default if no 1 is found
            
            while low <= high:
                mid = (low + high) // 2
                if arr[i][mid] == 1:
                    first_one_index = mid
                    high = mid - 1  # Look for a potential 1 further to the left
                else:
                    low = mid + 1
            
            # Number of 1s in this row is total columns minus the first 1's index
            count_1s = m - first_one_index
            
            # We only update if we strictly find MORE 1s than before
            if count_1s > max_1s_count:
                max_1s_count = count_1s
                max_1s_row = i
                
        return max_1s_row
