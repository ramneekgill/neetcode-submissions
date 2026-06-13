class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {} #(r,c)
        
        max_val = 0
        def dfs(r,c,prev, cur):
            if r<0 or c<0 or r>=len(matrix) or c>=len(matrix[0]) or prev >= matrix[r][c]:
                return cur
            # if (r,c) in dp:
            #     print('r: ' + str(r) + ' c:' + str(c) + ' dp[(r,c)]: ' + str(dp[(r,c)]) + ' cur: ' + str(cur))
            #     return dp[(r,c)] + cur
            cur += 1
            val = max(dfs(r+1,c,matrix[r][c], cur), dfs(r-1,c,matrix[r][c], cur), dfs(r,c+1,matrix[r][c], cur), dfs(r,c-1,matrix[r][c], cur))
            dp[(r,c)] = val
            return val


        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                val = dfs(r,c,-1,0)
                max_val = max(max_val, val)
                
        return max_val
        