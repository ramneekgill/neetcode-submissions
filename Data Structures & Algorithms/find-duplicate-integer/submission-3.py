class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [0] * (len(nums)-1)
        for num in nums:
            if seen[num - 1]:
                return num
            seen[num - 1] = 1
        return -1

            
        