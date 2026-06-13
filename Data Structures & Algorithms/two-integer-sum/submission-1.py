class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for x in range(len(nums)):
            diff = target-nums[x]
            if diff in targets:
                return [targets[diff], x]
            targets[nums[x]] = x
            
        return -1



        