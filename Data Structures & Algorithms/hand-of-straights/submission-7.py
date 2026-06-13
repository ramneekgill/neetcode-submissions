class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize > 0:
            return False
        
        dic = {}
        for n in hand:
            dic[n] = 1 + dic.get(n,0)
        
        heap = list(dic.keys())
        heapq.heapify(heap)
        while heap:
            first = heap[0]
            for i in range(first, first+groupSize):
                if i not in dic:
                    return False
                dic[i] -= 1
                if dic[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True









        