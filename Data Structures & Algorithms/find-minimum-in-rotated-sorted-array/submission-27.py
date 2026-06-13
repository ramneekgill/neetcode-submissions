class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        ans = nums[0]

        while l<r:
            mid = (l+r)//2
            ans = min(nums[mid], ans)
            if nums[mid]>nums[r]:
                l = mid + 1
            elif nums[mid]<=nums[r]:
                r = mid - 1
        
        return min(ans, nums[l])