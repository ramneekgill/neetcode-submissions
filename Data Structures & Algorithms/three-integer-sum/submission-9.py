class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort and 3 pointer?
        #3 pointer without sorting?

        nums.sort()
        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    total = nums[i]+nums[j]+nums[k]
                    if total == 0:
                        res.add((nums[i], nums[j], nums[k]))
        return list(res)
                    
                    
        