class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])

        for i in range(len(nums)-3,-1,-1):
            nums[i] = max(nums[i+1], nums[i]+nums[i+2])
        return nums[0]
        

        
        