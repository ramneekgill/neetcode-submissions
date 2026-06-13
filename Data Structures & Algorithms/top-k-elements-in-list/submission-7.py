class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1
        h = []
        for key,v in hm.items():
            heapq.heappush(h, (v,key))
            if len(h) > k:
                heapq.heappop(h)
        return [num for freq,num in h]
