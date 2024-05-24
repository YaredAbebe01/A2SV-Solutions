class Solution(object):
    def largestLocal(self, grid):
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]
        
        for i in range(n - 2):
            for j in range(n - 2):
                maxVal = 0
                for x in range(3):
                    for y in range(3):
                        maxVal = max(maxVal, grid[i + x][j + y])
                maxLocal[i][j] = maxVal
        
        return maxLocal
