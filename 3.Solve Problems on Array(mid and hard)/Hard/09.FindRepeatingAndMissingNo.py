#https://leetcode.com/problems/find-missing-and-repeated-values/submissions/2028348018/

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_numbers = n * n
        
        # Frequency array to count occurrences of numbers from 1 to n^2
        # Size is total_numbers + 1 so we can use 1-based indexing directly
        count = [0] * (total_numbers + 1)
        
        # Step 1: Count frequencies of each number in the grid
        for row in grid:
            for num in row:
                count[num] += 1
                
        repeated = -1
        missing = -1
        
        # Step 2: Identify the repeated and missing numbers
        for i in range(1, total_numbers + 1):
            if count[i] == 2:
                repeated = i
            elif count[i] == 0:
                missing = i
                
        return [repeated, missing]
