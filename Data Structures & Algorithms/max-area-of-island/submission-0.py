class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()

        def dfs(r,c, area):
            if(r<0 or c<0 or r==len(grid) or c==len(grid[0])
                or (r,c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r,c))
            return 1 + dfs(r+1,c,area) + dfs(r-1,c,area) + dfs(r,c+1,area) + dfs(r,c-1,area)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == 1:
                    new_a = dfs(r,c,0)
                    max_area = max(max_area, new_a)
        return max_area
        