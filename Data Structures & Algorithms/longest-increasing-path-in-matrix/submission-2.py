class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {} #(r,c)
        
        max_val = 0
        def dfs(r,c,prev, cur):
            if r<0 or c<0 or r>=len(matrix) or c>=len(matrix[0]) or (r,c) in visit or prev >= matrix[r][c]:
                return cur
            if (r,c) in dp:
                return dp[(r,c)] + cur
            if prev < matrix[r][c]:
                cur += 1
            #print('visiting row ' + str(r) + ' column ' + str(c) + ' cur is ' + str(cur))
            visit.add((r,c))
            val = max(dfs(r+1,c,matrix[r][c], cur), dfs(r-1,c,matrix[r][c], cur), dfs(r,c+1,matrix[r][c], cur), dfs(r,c-1,matrix[r][c], cur))
            visit.remove((r,c))
            return val

        # visit = set()
        # max_val = dfs(0,0,-1,0)
        visit = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                val = dfs(r,c,-1,0)
                dp[(r,c)] = val
                # if(r == 1 and c in [0,1,2]):
                #     print('r: ' + str(r) + ' c:' + str(c) + ' val:' + str(val))
                # if(r == 2 and c == 0):
                #     print('r: ' + str(r) + ' c:' + str(c) + ' val:' + str(val))
                max_val = max(max_val, val)
                
        return max_val
        