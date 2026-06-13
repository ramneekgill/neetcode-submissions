class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            mid = l + (r-l)//2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:# same ramp
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:# mid is on second ramp
                if nums[mid] < target and nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1




        