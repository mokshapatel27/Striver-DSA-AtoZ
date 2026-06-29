#https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        #CREATES EMPTY GRID OF N*N
        board = [["."] * n for _ in range(n)]
        
        # Lookups for attacks in O(1) time
        cols = set()
        pos_diag = set()  # (r + c) constant along anti-diagonals
        neg_diag = set()  # (r - c) constant along main diagonals
        
        def backtrack(r):
            # Base case: All queens placed successfully
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                # If the cell is under attack, skip it
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # Place the queen and flag the paths
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                
                # Move to the next row
                backtrack(r + 1)
                
                # Backtrack: Remove the queen and unflag the paths
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
                
        backtrack(0)
        return res
