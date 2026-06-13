class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l + (r-l)//2)
            if nums[l] > nums[r]:
                if nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    r = mid
            else:
                return nums[l]
        return nums[l]



        