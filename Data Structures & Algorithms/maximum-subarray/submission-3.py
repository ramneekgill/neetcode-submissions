class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        cur_sum = 0
        for n in nums:
            cur_sum = max(n, cur_sum+n)
            res = max(res, cur_sum)
        return res


        