class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = 0
        final_max = float('-inf')
        for n in nums:
            curr_max = max(curr_max+n, n)
            final_max = max(final_max, curr_max)
        return final_max
        