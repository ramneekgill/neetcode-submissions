class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob1, rob2 = 0,0
        for i in range(len(nums)-1):
            tmp = max(nums[i]+rob1,rob2)
            rob1 = rob2
            rob2 = tmp
        
        first = rob2

        rob1, rob2 = 0, 0
        for i in range(1,len(nums)):
            tmp = max(nums[i]+rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        
        return max(first, rob2)

        