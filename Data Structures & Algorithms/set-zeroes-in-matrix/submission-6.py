class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rows, cols = [False]*m, [False]*n

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        
        for r in range(m):
            for c in range(n):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0

        
        