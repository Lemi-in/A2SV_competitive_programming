class Solution:
    def countUnguarded(self, m, n, guards, walls):
        grid = [[0]*n for _ in range(m)]
        G , W, GC  = 1 , 2 , 3
        for r, c in guards:
            grid[r][c] = G
        for r,c in walls:
            grid[r][c] = W
        
        #left to  right
        for r in range(m):
            pos = 0
            for c in range(n):
                if grid[r][c] == G:
                    pos = GC 
                elif grid[r][c] == W:
                    pos = 0 
                else:
                    if pos == GC:
                        grid[r][c] = GC
        
        #right to left
        for r in range(m):
            pos = 0
            for c in range(n-1, -1 , -1):
                if grid[r][c] == G:
                    pos = GC 
                elif grid[r][c] == W:
                    pos = 0 
                else:
                    if pos == GC:
                        grid[r][c] = GC
        
        #top to bottom
        for c in range(n):
            pos = 0
            for r in range(m):
                if grid[r][c] == G:
                    pos = GC 
                elif grid[r][c] == W:
                    pos = 0
                else:
                    if pos == GC:
                        grid[r][c] = GC
        
        #bottom to top
        for c in range(n):
            pos = 0
            for r in range(m-1, -1, -1):
                if grid[r][c] == G:
                    pos = GC 
                elif grid[r][c] == W:
                    pos = 0
                else:
                    if pos == GC:
                        grid[r][c] = GC
        
        count = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    count+=1
        
        return count






        
        
