#https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_col_zero = False
        
        # Step 1: Scan the matrix and use the 1st row/col as markers
        for r in range(m):
            if matrix[r][0] == 0:
                first_col_zero = True
                
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0  # Fixed: changed == to =
                    matrix[0][c] = 0  # Fixed: changed == to =

        # Step 2: NEW - Use those markers to set inner cells to zero
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Step 3: Handle the 1st row flag separately
        if matrix[0][0] == 0:
            for c in range(n):
                matrix[0][c] = 0

        # Step 4: Handle the 1st column flag separately
        if first_col_zero:
            for r in range(m):
                matrix[r][0] = 0
