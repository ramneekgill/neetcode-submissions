class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            check = target-nums[i]
            if check in dic:
                return [dic[check], i]
            dic[nums[i]] = i
        