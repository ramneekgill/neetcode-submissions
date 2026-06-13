class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        mi, ma = 1,1

        for n in nums:
            tmp = ma*n
            ma = max(n, ma*n, mi*n)
            mi = min(n, tmp, mi*n)
            res = max(res, ma)
        
        return res
        