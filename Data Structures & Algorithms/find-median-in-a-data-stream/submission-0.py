class MedianFinder:

    def __init__(self):
        self.smallheap = []
        self.largeheap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallheap, -num)
        if self.largeheap and self.smallheap[0] > self.largeheap[0]:
            val = -heapq.heappop(self.smallheap)
            heapq.heappush(self.largeheap,val)
        if len(self.smallheap) > len(self.largeheap):
            val = -heapq.heappop(self.smallheap)
            heapq.heappush(self.largeheap,val)
        if len(self.largeheap) > len(self.smallheap):
            val = -heapq.heappop(self.largeheap)
            heapq.heappush(self.smallheap,val)

        
    def findMedian(self) -> float:
        if len(self.smallheap) > len(self.largeheap):
            return -self.smallheap[0]
        elif len(self.largeheap) > len(self.smallheap):
            return self.largeheap[0]
        else:
            print(-self.smallheap[0])
            print(self.largeheap[0])
            return (-self.smallheap[0]+self.largeheap[0])/2.0
        
        