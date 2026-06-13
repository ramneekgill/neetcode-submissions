class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        ans = float('inf')
        # if len(nums) == 1:
        #     return nums[0]
        # if nums[r] > nums[0]:
        #     return nums[0]
        while l<r:
            mid = (l+r)//2
            ans = min(ans, nums[mid])
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1  
        

        return min(ans, nums[l])