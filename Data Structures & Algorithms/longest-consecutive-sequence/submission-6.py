class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            if (num-1) not in numsSet:
                length = 1
                cur = num
                while (cur + 1) in numsSet:
                    length+=1
                    cur+=1
                longest = max(longest, length)
        return longest
                

            
            
            

        

            
                

        