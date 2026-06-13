class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        
        max_val = 0
        def dfs(r,c,prev):
            if r<0 or c<0 or r>=len(matrix) or c>=len(matrix[0]) or prev >= matrix[r][c]:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]

            val = max(1+dfs(r+1,c,matrix[r][c]), 1+dfs(r-1,c,matrix[r][c]), 1+dfs(r,c+1,matrix[r][c]), 1+dfs(r,c-1,matrix[r][c]))
            dp[(r,c)] = val
            return val

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                val = dfs(r,c,-1)
                max_val = max(max_val, val)
        return max_val
        