class Solution(object):
    def transpose(self, matrix):
        x = len(matrix)
        y = len(matrix[0])
        ans = [[0 for n in range(x)] for m in range(y)]
        for i in range(x):
            for j in range(y):
                ans[j][i] = matrix[i][j]
        return ans
