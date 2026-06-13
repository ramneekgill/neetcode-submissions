class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}
        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            for j in range(i+1, len(points)):
                x2 = points[j][0]
                y2 = points[j][1]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append([j, dist])
                adj[j].append([i, dist])
        
        cost = 0
        mHeap = [[0,0]]
        visited = set()
        while len(visited) < len(points):
            dist, pnt = heapq.heappop(mHeap)
            if pnt in visited:
                continue
            visited.add(pnt)
            cost += dist
            for nei, neiCost in adj[pnt]:
                if nei not in visited:
                    heapq.heappush(mHeap, [neiCost, nei])
        return cost

        