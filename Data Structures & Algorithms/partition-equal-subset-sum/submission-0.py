class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums)//2
        for i in range(len(nums)-1,-1,-1):
            new_dp = set()
            for t in dp:
                new_dp.add(t+nums[i])
                new_dp.add(t)
            dp = new_dp
        return True if target in dp else False
                
        