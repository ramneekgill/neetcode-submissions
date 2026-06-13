class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        cur_area = 0
        def dfs(r,c):
            nonlocal cur_area
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or (r,c) in visited or grid[r][c] == 0:
                return
            cur_area += 1
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0 and (r,c) not in visited:
                    dfs(r,c)
                    max_area = max(max_area, cur_area)
                    cur_area = 0

        return max_area
        