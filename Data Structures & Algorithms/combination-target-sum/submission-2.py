class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(arr, total, i):
            if i >= len(nums) or total > target:
                return
            if total == target:
                res.append(arr.copy())
                return
            arr.append(nums[i])
            backtrack(arr, total+nums[i], i)
            arr.pop()
            backtrack(arr, total, i+1)
        
        backtrack([], 0, 0)
        return res
        