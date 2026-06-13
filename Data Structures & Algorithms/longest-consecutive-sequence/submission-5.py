class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_count = 0
        nums.sort()
        i = 0
        cur, streak = nums[0], 0
        while i < len(nums):
            if cur != nums[i]:
                streak = 0
                cur = nums[i]
            
            while i < len(nums) and nums[i] == cur:
                i+=1
            streak += 1
            cur += 1
            max_count = max(streak, max_count)
        return max_count

            
            
            

        

            
                

        