class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set([0,0])
        minH = [[grid[0][0],0,0]]
        def addSquare(r,c,h):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or (r,c) in visited:
                return
            visited.add((r,c))
            heapq.heappush(minH, [(max(h, grid[r][c])),r,c])

        while minH:
            h,r,c = heapq.heappop(minH)
            if r == N-1 and c == N-1:
                return h
            addSquare(r+1,c,h)
            addSquare(r,c+1,h)
            addSquare(r-1,c,h)
            addSquare(r,c-1,h)
        return -1
            