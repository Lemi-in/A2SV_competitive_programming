class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        local = []
        n = len(grid)
        m = n - 2
        for i in range(m):
            localRow = []
            for j in range(m):
                submat = [grid[i + r][j:j + 3] for r in range(3)]
                maxval = max(max(row) for row in submat)
                localRow.append(maxval)
            local.append(localRow)
        return local
