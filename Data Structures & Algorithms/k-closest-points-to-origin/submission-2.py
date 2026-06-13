class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ls = []
        for point in points:
            d = ((point[0]**2) + (point[1]**2))**0.5
            ls.append([d, point])
        heapq.heapify(ls)
        res = []
        while k > 0:
            res.append(heapq.heappop(ls)[1])
            k-=1
        return res


        