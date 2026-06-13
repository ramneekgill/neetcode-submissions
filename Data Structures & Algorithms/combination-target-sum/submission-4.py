class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(arr, total, i):
            if total == target:
                res.append(arr.copy())
                return
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                arr.append(nums[j])
                backtrack(arr, total+nums[j], j)
                arr.pop()
        
        backtrack([], 0, 0)
        return res
        