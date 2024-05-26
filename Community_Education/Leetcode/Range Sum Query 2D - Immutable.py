class NumMatrix:
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0 for i in range(n+1)] for j in range(m+1)]
        
        for r in range(1,m+1):
            for c in range(1,n+1):
                self.prefix[r][c] = matrix[r-1][c-1] + self.prefix[r][c-1]

    def sumRegion(self, row1, col1, row2, col2):
        summ = 0
        for r in range(row1+1, row2+2):
            summ += self.prefix[r][col2+1] - self.prefix[r][col1]  
        return summ

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
