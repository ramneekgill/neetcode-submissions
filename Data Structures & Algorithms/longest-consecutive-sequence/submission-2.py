class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for x in nums_set:
            if (x-1) not in nums_set:
                length = 1
                while (x+ length) in nums_set:
                    length += 1
                longest = max(longest, length)
        return longest

        

        