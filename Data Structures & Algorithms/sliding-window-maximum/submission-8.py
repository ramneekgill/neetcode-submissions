class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #max num can be changed on window move in two scenarios:
        #current max leaves on left edge
        #new max number enters on right edge
        if len(nums) < k:
            return [max(nums)]
        mx = []

        for i in range(len(nums)-(k-1)):
            mx.append(max(nums[i:i+k]))
        return mx



        