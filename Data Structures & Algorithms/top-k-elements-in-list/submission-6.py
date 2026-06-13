class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0) + 1
        
        min_heap = []
        for key,val in dic.items():
            min_heap.append([-val,key])
        
        heapq.heapify(min_heap)
        res = []
        for i in range(k):
            val, key = heapq.heappop(min_heap)
            res.append(key)
        return res

        