class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [[0,k]]
        adj = defaultdict(list)
        visited = set()
        for s,d,t in times:
            adj[s].append([d,t])
        
        res = 0
        while heap:
            w1,n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            visited.add(n1)
            res = max(res, w1)
            for n2,w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(heap, [w1+w2, n2])
        
        return res if len(visited) == n else -1

        