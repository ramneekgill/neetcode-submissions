class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if len(nums) < k:
        #     return [max(nums)]
        # mx = []
        # mx_heap = []
        # to_delete = Counter()

        # for i in range(k):
        #     heapq.heappush(mx_heap, -nums[i])
        # mx.append(-mx_heap[0])
        # l = 0
        # for r in range(k, len(nums)):
        #     to_delete[nums[l]] += 1
        #     heapq.heappush(mx_heap, -nums[r])
        #     while mx_heap and to_delete[-mx_heap[0]] > 0:
        #         val = -heapq.heappop(mx_heap)
        #         to_delete[val] -= 1
        #     mx.append(-mx_heap[0])
        #     l+=1
        # return mx
        # if len(nums) < k:
        #     return [max(nums)]
        mx = []

        for i in range(len(nums)-(k-1)):
            mx.append(max(nums[i:i+k]))
        return mx




    

        