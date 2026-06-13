class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort and 3 pointer?
        #3 pointer without sorting?

        nums.sort()
        #res = set()
        res = []
        i = 0
        while i < len(nums)-2 and nums[i] <= 0:
            if i>0 and nums[i] == nums[i-1]:
                i+=1
                continue
            j = i+1
            k = len(nums)-1
            
            while j<k:
                if j>(i+1) and nums[j] == nums[j-1]:
                    j+=1
                    continue
                total = nums[i]+nums[j]+nums[k]
                if total == 0:
                    res.append((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                if j<k and total < 0:
                    j+=1
                    continue
                elif j<k and total > 0:
                    k-=1
                    continue
            i+=1
        return res
                    
                    
        