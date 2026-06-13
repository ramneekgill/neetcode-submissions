class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort and 3 pointer?
        #3 pointer without sorting?

        nums.sort()
        res = set()
        i = 0
        while i < len(nums)-2 and nums[i] <= 0:
            j = i+1
            k = len(nums)-1
            while j<k:
                total = nums[i]+nums[j]+nums[k]
                if total == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                if j<k and total < 0:
                    j+=1
                    continue
                elif j<k and total > 0:
                    k-=1
                    continue
            i+=1
        return list(res)
                    
                    
        