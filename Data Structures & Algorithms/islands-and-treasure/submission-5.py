class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        dist = 1
        def add(r,c):
            nonlocal dist
            if (r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or (r,c) in visited
                or grid[r][c] == -1):
                return
            q.append((r,c))
            visited.add((r,c))
            grid[r][c] = dist

        while q: 
            for _ in range(len(q)):
                r,c = q.popleft()
                add(r+1,c)
                add(r-1,c)
                add(r,c+1)
                add(r,c-1)
            dist+=1