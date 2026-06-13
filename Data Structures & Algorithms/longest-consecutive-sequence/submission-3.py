class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        counts = set(nums)
        for num in nums:
            curr = num
            streak = 0
            while curr in counts:
                curr += 1
                streak += 1
            max_count = max(streak, max_count)
        return max_count

            
                

        