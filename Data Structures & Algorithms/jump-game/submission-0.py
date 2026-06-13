class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[len(nums)-1] = True
        for i in range(len(nums)-2,-1,-1):
            count = nums[i]
            if i+count >= len(nums)-1:
                dp[i] = True
            else:
                while count > 0:
                    if dp[i+count]:
                        dp[i] = True
                    count-=1
        return dp[0]

        