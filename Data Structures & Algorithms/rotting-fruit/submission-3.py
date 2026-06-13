class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0

        def addcell(r,c):
            nonlocal fresh
            if(r<0 or c<0 or r==len(grid) or c==len(grid[0])
                or grid[r][c] != 1):
                return
            grid[r][c] = 2
            fresh -= 1
            q.append([r,c])
        
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        

        second = 0
        while fresh > 0 and q:
            for _ in range(len(q)):
                r,c = q.popleft()
                addcell(r+1,c)
                addcell(r-1,c)
                addcell(r,c+1)
                addcell(r,c-1)
            second += 1

        return second if fresh == 0 else -1

        