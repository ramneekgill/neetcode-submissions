class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_ls = {i:[] for i in range(1,n+1)}
        for src,dest,time in times:
            adj_ls[src].append((dest, time))

        min_heap = [(0,k)]
        visit = set()
        t = 0
        while min_heap:
            w1,n1 = heapq.heappop(min_heap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1
            for nei,w2 in adj_ls[n1]:
                if nei in visit:
                    continue
                heapq.heappush(min_heap, (w1+w2, nei))
        return t if len(visit) == n else -1
            

            


        