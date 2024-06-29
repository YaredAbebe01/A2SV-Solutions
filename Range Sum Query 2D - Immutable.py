class NumMatrix:
    def __init__(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        self.ps = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                self.ps[r + 1][c + 1] = (self.ps[r][c + 1] + self.ps[r + 1][c] - self.ps[r][c] + matrix[r][c])

    def sumRegion(self, row1, col1, row2, col2):
        return (self.ps[row2 + 1][col2 + 1] - self.ps[row1][col2 + 1] -
                self.ps[row2 + 1][col1] + self.ps[row1][col1])
