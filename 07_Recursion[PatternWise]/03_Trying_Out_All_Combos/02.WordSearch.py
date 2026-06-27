#https://leetcode.com/problems/word-search/description/

#LEFT

class Solution:
    def exist(self, board: List[List[str]], word: str, r: int = None, c: int = None) -> bool:
        # Base Case: Entire word matched successfully
        if not word:
            return True
            
        ROWS, COLS = len(board), len(board[0])
        
        # KICK-OFF STEP: If r and c are None, search for the first letter
        if r is None and c is None:
            for i in range(ROWS):
                for j in range(COLS):
                    if board[i][j] == word[0]:
                        if self.exist(board, word, i, j):
                            return True
            return False
            
        # RECURSIVE STEP: Validate boundaries and character matching
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[0]:
            return False
            
        # Mark cell as visited
        temp = board[r][c]
        board[r][c] = "#"
        
        # Explore 4 directions with the remainder of the word
        found = (self.exist(board, word[1:], r + 1, c) or
                 self.exist(board, word[1:], r - 1, c) or
                 self.exist(board, word[1:], r, c + 1) or
                 self.exist(board, word[1:], r, c - 1))
                 
        # Backtrack: Restore the cell
        board[r][c] = temp
        
        return found
