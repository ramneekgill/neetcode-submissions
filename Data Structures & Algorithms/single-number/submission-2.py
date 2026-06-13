class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        dups = sum(list(set(nums)))
        res = dups - (total-dups)
        return res