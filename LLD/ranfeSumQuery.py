class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_sum = [[0 for i in range(len(self.matrix[0]))] for j in range(len(self.matrix[0]))]\
        add = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                add += self.matrix[i][j]
                self.prefix_sum[i][j] = add


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.prefix_sum[row2][col2]
        elif row1 == 0:
            return self.prefix_sum[row2][col2] - self.prefix_sum[row2][col1-1]
        elif col1 == 0:
            return self.prefix_sum[row2][col2] - self.prefix_sum[row1-1][col2]
        else:
            return self.prefix_sum[row2][col2] - self.prefix_sum[row1-1][col2] - self.prefix_sum[row2][col1-1] + self.prefix_sum[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)