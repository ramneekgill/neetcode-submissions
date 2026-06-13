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
        return -neg_stones[0] if neg_stones else 0

        