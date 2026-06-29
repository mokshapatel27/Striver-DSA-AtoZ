#https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

class Solution:
    def ratInMaze(self, maze, r=0, c=0, path="") -> list[str]:
        n = len(maze)
        
        #MZE BORDERS AND BLOCKED PATH
        if r < 0 or c < 0 or r >= n or c >= n or maze[r][c] == 0:
            return []
            
        # 2. Destination Reached
        if r == n - 1 and c == n - 1:
            return [path]
            
        # 3. Backtracking Step
        maze[r][c] = 0  # Mark visited
        
        # Explore in lexicographical order: D -> L -> R -> U
        paths = []
        paths.extend(self.ratInMaze(maze, r + 1, c, path + 'D'))  # Down
        paths.extend(self.ratInMaze(maze, r, c - 1, path + 'L'))  # Left
        paths.extend(self.ratInMaze(maze, r, c + 1, path + 'R'))  # Right
        paths.extend(self.ratInMaze(maze, r - 1, c, path + 'U'))  # Up
        
        maze[r][c] = 1  # Unmark visited (Backtrack)
        
        return paths
