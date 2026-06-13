class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def add_room(r,c):
            if(r <0 or c<0 or r==len(grid) or c==len(grid[0]) or
                (r,c) in visited or grid[r][c] == -1):
                return
            visited.add((r,c))
            q.append([r,c])

        q = deque()
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                add_room(r+1,c)
                add_room(r-1,c)
                add_room(r,c+1)
                add_room(r,c-1)
            dist += 1

            


        




        