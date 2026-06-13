class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def dfs(r,c):
            matrix[r][c] = -1
            for v in range(len(matrix)):
                if(matrix[v][c] == 0):
                    dfs(v,c)
                matrix[v][c] = -1
            for h in range(len(matrix[0])):
                if(matrix[r][h] == 0):
                    dfs(r,h)
                matrix[r][h] = -1

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    dfs(r,c)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == -1:
                    matrix[r][c] = 0