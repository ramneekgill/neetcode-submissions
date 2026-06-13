class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_total = sum(nums)
        actual_total = 0
        for i in range(len(nums)+1):
            actual_total +=i

        return actual_total-nums_total


        