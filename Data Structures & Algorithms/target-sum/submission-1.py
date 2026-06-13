class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i,total):
            if total == target and i == len(nums):
                return 1
            if i>=len(nums):
                return 0
            if (i,total) in dp:
                return dp[(i,total)]
            
            res = 0
            res += dfs(i+1,total+nums[i])
            res += dfs(i+1,total-nums[i])
            dp[(i,total)] = res
            return dp[(i,total)]
        return dfs(0,0)
            


        