class Solution:
    

    def swimInWater(self, grid: List[List[int]]) -> int:
        def get_neighbors(r,c,t):
            if(r<0 or c<0 or r==len(grid) or c==len(grid)
                or (r,c) in visit):
                return
            visit.add((r,c))
            heapq.heappush(min_heap, (max(t,grid[r][c]),r,c))
        min_heap = [(grid[0][0],0,0)]
        visit = set()
        visit.add((0,0))
        while min_heap:
            t,r,c = heapq.heappop(min_heap)
            if r==len(grid)-1 and c==len(grid)-1:
                return t
            get_neighbors(r+1,c,t)
            get_neighbors(r-1,c,t)
            get_neighbors(r,c+1,t)
            get_neighbors(r,c-1,t)

            
            
            
        




        