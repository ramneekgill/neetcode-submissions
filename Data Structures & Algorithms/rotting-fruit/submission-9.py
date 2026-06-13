class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fruit_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fruit_count += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        if fruit_count == 0:
            return 0
        
        def add_cell(r,c):
            nonlocal fruit_count
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c] == 0 or grid[r][c] == 2:
                return
            grid[r][c] = 2
            fruit_count -= 1
            q.append((r,c))
            
        mins = 0
        while fruit_count > 0 and q:
            prev_count = fruit_count
            for _ in range(len(q)):
                r,c = q.popleft()
                add_cell(r+1,c)
                add_cell(r-1,c)
                add_cell(r,c+1)
                add_cell(r,c-1)
            mins+=1
        return -1 if fruit_count else mins



        