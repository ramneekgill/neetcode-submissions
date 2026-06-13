class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_min, cur_max = 1,1

        for n in nums:
            tmp = cur_max * n
            cur_max = max(n*cur_max, n*cur_min, n) # 15
            cur_min = min(tmp, n*cur_min, n) # 0
            res = max(res, cur_max) # 15
        return res
        