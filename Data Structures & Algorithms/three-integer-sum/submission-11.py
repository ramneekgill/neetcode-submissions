class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort and 3 pointer?
        #3 pointer without sorting?

        nums.sort()
        res = set()
        i = 0
        while i < len(nums) and nums[i] <= 0:
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    total = nums[i]+nums[j]+nums[k]
                    if total == 0:
                        res.add((nums[i], nums[j], nums[k]))
            i+=1
        return list(res)
                    
                    
        