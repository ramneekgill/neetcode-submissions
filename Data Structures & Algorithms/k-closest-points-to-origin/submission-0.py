class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        m_heap = []
        for i,(x,y) in enumerate(points):
            dist = math.sqrt((x-0)**2 + (y-0)**2)
            heapq.heappush(m_heap,(dist, i))
        ls = []
        while k > 0:
            _,i = heapq.heappop(m_heap)
            ls.append(points[i])
            k-=1
        return ls


        