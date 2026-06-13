class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        check = set(nums)
        for i in range(len(nums)):
            curr_length = 0
            num = nums[i]
            if (num-1) in check:
                continue
            while num in check:
                curr_length+=1
                num += 1
            max_length = max(max_length, curr_length)
        return max_length



        