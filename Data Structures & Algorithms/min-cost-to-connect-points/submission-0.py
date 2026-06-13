class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_ls = {i:[] for i in range(len(points))}
        
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i+1,len(points)):
                xj,yj = points[j]
                dist = abs(xi-xj)+abs(yi-yj)
                adj_ls[i].append([dist,j])
                adj_ls[j].append([dist,i])
        
        res = 0
        visit = set()
        min_heap = [[0,0]]

        while len(visit) < len(points):
            cost, node = heapq.heappop(min_heap)
            if node in visit:
                continue
            visit.add(node)
            res += cost
            for nei_cost,nei in adj_ls[node]:
                if nei in visit:
                    continue
                heapq.heappush(min_heap, [nei_cost,nei])
        return res


        