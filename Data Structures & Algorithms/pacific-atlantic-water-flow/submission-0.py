class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        res = []
        curr = [0,0]
        visited = set()
        def dfs(r,c):
            if (r,c) in visited:
                return
            if r<0 or c<0:
                curr[0] = 1
                return
            if r == len(heights) or c == len(heights[0]):
                curr[1] = 1
                return
            if curr[0] == 1 and curr[1] == 1:
                return
            visited.add((r,c))
            if (r+1 < len(heights) and heights[r+1][c] <= heights[r][c]) or r+1==len(heights):
                dfs(r+1,c)
            if (r-1 >= 0 and heights[r-1][c] <= heights[r][c]) or r-1<0:
                dfs(r-1,c)
            if (c+1 < len(heights[0]) and heights[r][c+1] <= heights[r][c]) or c+1 == len(heights[0]):
                dfs(r,c+1)
            if (c-1 >= 0 and heights[r][c-1] <= heights[r][c]) or c-1<0:
                dfs(r,c-1)

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                dfs(r,c)
                if curr[0] == 1 and curr[1] == 1:
                    res.append([r,c])
                curr = [0,0]
                visited = set()
        
        return res
        
            

        