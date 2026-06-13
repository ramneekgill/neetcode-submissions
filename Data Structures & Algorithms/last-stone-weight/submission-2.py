class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-stone for stone in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            stone_1 = -heapq.heappop(neg_stones)
            stone_2 = -heapq.heappop(neg_stones)
            diff = abs(stone_1-stone_2)
            if diff:
                heapq.heappush(neg_stones, -diff)
        if len(neg_stones) == 1:
            return -neg_stones[0]
        return 0

        