class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        hp = []

        for i in range(len(nums)):
            heapq.heappush(hp, [-nums[i],i])

            if i>=(k-1):
                while hp[0][1] <= (i-k):
                    heapq.heappop(hp)
                res.append(-hp[0][0])
        return res




    

        