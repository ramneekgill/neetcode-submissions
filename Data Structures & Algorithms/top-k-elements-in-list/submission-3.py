class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        max_heap = []
        res = []
        for key,val in dic.items():
            heapq.heappush(max_heap, [-val,key])
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res



        