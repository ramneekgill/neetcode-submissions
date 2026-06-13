class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 0
        hm = {}
        for idx,n in enumerate(nums):
            check = target-n
            if check in hm:
                return [hm[check], idx]
            hm[n] = idx
        return [-1,-1]
        