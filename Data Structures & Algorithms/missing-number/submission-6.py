class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)+1
        expected_total = 0
        for i in range(1,n):
            expected_total += i


        curr_total = sum(nums)
        return expected_total-curr_total

        