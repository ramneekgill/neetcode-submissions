class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,ele in enumerate(nums):
            if ele > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                three_sum = ele+nums[l]+nums[r]
                if three_sum > 0:
                    r-=1
                elif three_sum < 0:
                    l+=1
                else:
                    res.append([ele,nums[l],nums[r]])
                    r-=1
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res
                
                
            
            


        