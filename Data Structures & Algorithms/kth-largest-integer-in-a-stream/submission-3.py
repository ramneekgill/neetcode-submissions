class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[:k]
        heapq.heapify(self.heap)
        for num in nums[k:]:
            if num > self.heap[0]:
                heapq.heappushpop(self.heap, num)
        self.k = k

        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
        
