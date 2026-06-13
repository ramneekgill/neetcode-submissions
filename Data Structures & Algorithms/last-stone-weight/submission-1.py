class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            if x>y:
                z = x-y
                heapq.heappush(max_heap, -z)
        return -heapq.heappop(max_heap) if len(max_heap) > 0 else 0

        