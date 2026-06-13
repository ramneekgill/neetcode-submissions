class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        res = []

        def dfs(r,c,prevHeight, visited):
            if (r<0 or c<0 or r>=len(heights) or c>=len(heights[0]) or 
                (r,c) in visited or heights[r][c] < prevHeight):
                return
            
            visited.add((r,c))
            dfs(r+1,c,heights[r][c], visited)
            dfs(r-1,c,heights[r][c], visited)
            dfs(r,c+1,heights[r][c], visited)
            dfs(r,c-1,heights[r][c], visited)
        
        for c in range(len(heights[0])):
            dfs(0,c,heights[0][c], pacific)
            dfs(len(heights)-1, c, heights[len(heights)-1][c], atlantic)

        for r in range(len(heights)):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, len(heights[0])-1, heights[r][len(heights[0])-1], atlantic)

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res

        